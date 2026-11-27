from django.db import models
from CustomerManagement.models import Customers
from Inventory.models import Products


class Orders(models.Model):
    customer_reference = models.ForeignKey(Customers, on_delete=models.CASCADE, null=True)
    product_reference = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    order_number = models.CharField(max_length=20,null = True)
    order_date = models.DateField(null = True)
    quantity = models.IntegerField(null = True,default=0)
    amount = models.FloatField(null = True,default=0.0)
    gst = models.FloatField(null = True,default=0.0)
    bill_amount = models.FloatField(null = True,default=0.0)

    def __str__(self):
        return self.order_number