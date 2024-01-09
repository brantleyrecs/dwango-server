from django.db import models
from .order import Order

class Revenue_Node(models.Model):
  order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name = 'order')
  total_order_amount = models.DecimalField(max_digits=7, decimal_places=2)
  tip_amount = models.DecimalField(max_digits=7, decimal_places=2)
  date_of_closure = models.DateField()
  payment_type = models.CharField(max_length=55)
