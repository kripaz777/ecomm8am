from django.urls import path
from .views import *


app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('subcategory/<slug>', SubCategoryView.as_view(), name='subcategory'),
    path('detail/<slug>', ItemDetailView.as_view(), name='detail'),


]
