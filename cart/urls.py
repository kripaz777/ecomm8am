from django.urls import path
from .views import *


app_name = 'cart'
urlpatterns = [
    path('cart', CartView.as_view(), name='cart'),
    path('add-to-cart/<slug>', cart, name='add-to-cart'),
    path('remove-cart/<slug>', remove_cart, name='remove-cart'),
    path('delete-cart/<slug>', delete_cart, name='delete-cart'),
    
]
