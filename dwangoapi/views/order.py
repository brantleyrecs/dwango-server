from django.http import HttpResponseServerError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import serializers, status
from dwangoapi.models import Order, User

class OrderView(ViewSet):
  
  def retrieve(self, request, pk):
    """getting single Order"""
    order = Order.objects.get(pk=pk)
    serializer = OrderSerializer(order)
    return Response(serializer.data)
  
  def list(self, request):
    """Getting all Orders"""
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    """Create Order"""
    user_id = User.objects.get(pk=request.data["userId"])
    
    order = Order.objects.create(
      user=user_id,
      customer_name=request.data["customerName"],
      phone_number=request.data["phoneNumber"],
      email=request.data["email"],
      order_type=request.data["orderType"],
      status=request.data["status"],
    )
    
    order.save()
    serializer = OrderSerializer(order)
    return Response(serializer.data)
  
  def update(self, request, pk):
    """Update Order"""
    order = Order.objects.get(pk=pk)
    order.customer_name=request.data["customerName"]
    order.phone_number=request.data["phoneNumber"]
    order.email=request.data["email"]
    order.order_type=request.data["orderType"]
    order.status=request.data["status"]
    
    user_id=User.objects.get(pk=request.data["userId"])
    order.user=user_id
    
    order.save()
    serializer = OrderSerializer(order)
    return Response(serializer.data)
  
  def destroy(self, request, pk):
    """Delete Order"""
    order = Order.objects.get(pk=pk)
    order.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)

class OrderSerializer(serializers.ModelSerializer):
  """serializer for Order"""
  class Meta:
    model=Order
    fields = ('id', 'customer_name', 'phone_number', 'email', 'order_type', 'status', 'user', 'items')
    depth = 2
