from django.urls import path,include
from .views import *

urlpatterns = [
    path('allproducts/',All_Products,name="allproducts"),
]
