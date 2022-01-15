from django.urls import include, path
from rest_framework import routers
from api import viewsets

router = routers.DefaultRouter()
router.register(r'store', viewsets.StoreViewset)
router.register(r'transaction', viewsets.TransactionsViewset)

urlpatterns = [
    path('', include(router.urls)),
]