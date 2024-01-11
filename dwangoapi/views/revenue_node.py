from django.http import HttpResponseServerError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import serializers, status
from dwangoapi.models import Revenue_Node, Order

class RevenueNodeView(ViewSet):
  def retrieve(self, request, pk):
    revenue = Revenue_Node.objects.get(pk=pk)
    serializer = RevenueSerializer(revenue)
    return Response(serializer.data)
    
  def list(self, request):
    revenues = Revenue_Node.objects.all()
    serializer = RevenueSerializer(revenues, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    """Create Revenue Node"""
    order_id = Order.objects.get(pk=request.data["orderId"])
    
    revenue = Revenue_Node.objects.create(
      order=order_id,
      total_order_amount=request.data["totalOrderAmount"],
      date_of_closure=request.data["dateOfClosure"],
      payment_type=request.data["paymentType"],
      tip_amount=request.data["tipAmount"],
    )
    
    revenue.save()
    serializer = RevenueSerializer(revenue)
    return Response(serializer.data)

class RevenueSerializer(serializers.ModelSerializer):
  class Meta:
    model=Revenue_Node
    fields = ('id', 'order', 'total_order_amount', 'date_of_closure', 'payment_type', 'tip_amount')
    depth = 2
