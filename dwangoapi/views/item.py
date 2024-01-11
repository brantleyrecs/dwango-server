from django.http import HttpResponseServerError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import serializers, status
from dwangoapi.models import Item

class ItemView(ViewSet):
  
  def retrieve(self, request, pk):
    """getting single Item"""
    item = Item.objects.get(pk=pk)
    serializer = ItemSerializer(item)
    return Response(serializer.data)
  
  def list(self, request):
    """Getting all Items"""
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    """Create Item"""
    
    item = Item.objects.create(
      name=request.data["name"],
      price=request.data["price"],
    )
    
    item.save()
    serializer = ItemSerializer(item)
    return Response(serializer.data)
  
  def update(self, request, pk):
    """Update Item"""
    item = Item.objects.get(pk=pk)
    item.name=request.data["name"]
    item.price=request.data["price"]
    
    item.save()
    serializer = ItemSerializer(item)
    return Response(serializer.data)

class ItemSerializer(serializers.ModelSerializer):
  """serializer for Item"""
  class Meta:
    model=Item
    fields = ('id', 'name', 'price')
    depth = 1
