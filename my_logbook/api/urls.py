from django.urls import include, path
from rest_framework import routers
from api import viewsets
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'file_origin', viewsets.FileOriginViewset, basename='file-origin')
router.register(r'store', viewsets.StoreViewset, basename='store')
router.register(r'transaction', viewsets.TransactionsViewset, basename='transaction')


urlpatterns = [
    path('', include(router.urls)),
    url(r'^store/(?P<store_id>.+)/amount/$', viewsets.StoreAmountView.as_view(), name='store-amount'),
]