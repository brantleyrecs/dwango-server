from rest_framework import serializers
from dwangoapi.models import Item

class ItemSerializer(serializers.ModelSerializer):
    
  class Meta:
    model = Item
    fields = ('id', 'name', 'price')
    depth = 0
