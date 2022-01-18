from rest_framework import viewsets, generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from oauth2_provider.contrib.rest_framework import OAuth2Authentication

from app.models import Transaction, Store, FileOrigin
from api.serializers import FileOriginSerializer, StoreSerializer, StoreTotalValuesSerializer, TransactionSerializer


class FileOriginViewset(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = FileOrigin.objects.all()
    serializer_class = FileOriginSerializer
    authentication_classes = [SessionAuthentication, OAuth2Authentication]
    permission_classes = [IsAuthenticated]


class StoreViewset(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    authentication_classes = [SessionAuthentication, OAuth2Authentication]
    permission_classes = [IsAuthenticated]


class StoreAmountView(generics.ListAPIView):
    lookup_url_kwarg = "store_id"
    serializer_class = StoreTotalValuesSerializer
    authentication_classes = [SessionAuthentication, OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        store_id = self.kwargs.get(self.lookup_url_kwarg)        
        store = Store.objects.filter(id=store_id)
        return store


class TransactionsViewset(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    authentication_classes = [SessionAuthentication, OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset
        store_id = self.request.GET.get('store_id', False)
        if store_id:
            queryset = queryset.filter(store__id=store_id)
        return queryset
