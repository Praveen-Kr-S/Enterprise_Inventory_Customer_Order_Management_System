from django.urls import path
from .views import *

urlpatterns = [
    path('allorders/',All_Orders,name="allorders"),
    path('addorder/',Add_Order,name="addorder"),
    path('updateorder/<int:pk>/',Update_Order,name="updateorder"),
    path('deleteorder/<int:pk>/',Delete_Order,name="deleteorder"),
]
