from django.urls import path, include
from rest_framework import routers, viewsets
from .views import ItemViewSet,ItemList
router = routers.DefaultRouter()
router.register(r'item', ItemViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('items', ItemList.as_view(), name='items'),

]