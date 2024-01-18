from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from dwangoapi.models import Order, Item, Order_Item

class OrderItemView(ViewSet):
    def retrieve(self, request, pk):
        """GET Single Order Item"""
        order_item = Order_Item.objects.get(pk=pk)
        serializer = OrderItemSerializer(order_item)
        return Response(serializer.data)
    
    def list(self, request):
      """GET All Song Genres"""
      order_items = Order_Item.objects.all()
      serializer = OrderItemSerializer(order_items, many=True)
      return Response(serializer.data)
  
    def destroy(self, request, pk):
        """Handles Delete request for an order item"""
        
        orderitem = Order_Item.objects.get(pk=pk)
        orderitem.delete()
        return Response(None)
    

class OrderItemSerializer(serializers.ModelSerializer):
    """JSON serializer for order items"""
    class Meta:
        model = Order_Item
        fields = ('id', 'order', 'item')
        depth = 1
