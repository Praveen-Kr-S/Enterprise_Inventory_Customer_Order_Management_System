from django.forms import ModelForm
from .models import Orders


class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = ['customer_reference','product_reference','order_number','order_date','quantity']