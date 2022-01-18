from rest_framework import routers
from api import viewsets
from django.urls import include, path


router = routers.DefaultRouter()
router.register('file_origin', viewsets.FileOriginViewset, basename='file-origin')
router.register('store', viewsets.StoreViewset, basename='store')
router.register('transaction', viewsets.TransactionsViewset, basename='transaction')


urlpatterns = [
    path('', include(router.urls)),
    path('store/<int:store_id>/amount/', viewsets.StoreAmountView.as_view(), name='store-amount')
]