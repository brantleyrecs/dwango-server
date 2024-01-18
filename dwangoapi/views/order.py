from django.http import HttpResponseServerError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import serializers, status
from dwangoapi.models import Order, User
from rest_framework.decorators import action
from dwangoapi.models import Item, Order_Item
from dwangoapi.serializers import ItemSerializer

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
  
  @action(methods=['post'], detail=True)
  def order_item(self, request, pk):
    """Method to post an item on a single order"""
    order_id = Order.objects.get(pk=pk)
    item_id = Item.objects.get(pk=request.data["item"])
    order_item = Order_Item.objects.create(
      order=order_id,
      item=item_id,
    )
    return Response(status=status.HTTP_201_CREATED)
  
  @action(methods=['get'], detail=True)
  def items(self, request, pk):
    """Method to get all the items associated to a single order"""
    items = Item.objects.all()
    associated_order = items.filter(order_id=pk)
    
    serializer = ItemSerializer(associated_order, many=True)
    return Response(serializer.data)
  
  # @action(methods=['delete', detail=True])
  # def remove_item(self, request, pk):
  #   order=Order.objects
class OrderItemSerializer(serializers.ModelSerializer):
  price = serializers.ReadOnlyField(source='item.price')
  name = serializers.ReadOnlyField(source='item.name')

  class Meta:
    model = Order_Item
    fields = ('id', 'price','name')

class OrderSerializer(serializers.ModelSerializer):
  """serializer for Order"""
  items = OrderItemSerializer(many=True, read_only=True)
  class Meta:
    model=Order
    fields = ('id', 'customer_name', 'phone_number', 'email', 'order_type', 'status', 'user', 'items')
    depth = 2
