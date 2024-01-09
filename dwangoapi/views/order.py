from django.http import HttpResponseServerError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import serializers, status
from dwangoapi.models import Order

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

class OrderSerializer(serializers.ModelSerializer):
  """serializer for Order"""
  class Meta:
    model=Order
    fields = ('id', 'customer_name', 'phone_number', 'email', 'order_type', 'status', 'user')
    depth = 1
