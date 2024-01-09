from django.db import models
from .user import User

class Order(models.Model):
  customer_name = models.CharField(max_length=50)
  phone_number = models.IntegerField()
  email=models.CharField(max_length=50)
  order_type=models.CharField(max_length=50)
  status=models.CharField(max_length=50)
  user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=0, related_name='user')
