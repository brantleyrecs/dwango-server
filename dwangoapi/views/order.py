from django.http import HttpResponseServerError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import serializers, status
from dwangoapi.models import Order

class OrderView(ViewSet):
  
  """getting single Order"""
  def retrieve(self, request, pk):
    order = Order.objects.get(pk=pk)
    serializer = OrderSerializer(order)
    return Response(serializer.data)
  
  """Getting all Orders"""
  def list(self, request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

"""serializer for Order"""
class OrderSerializer(serializers.ModelSerializer):
  class Meta:
    model=Order
    fields = ('id', 'customer_name', 'phone_number', 'email', 'order_type', 'status', 'user_id')
    depth = 1
