from rest_framework import viewsets
from app.models import Transaction, Store
from .serializers import TransactionSerializer, StoreSerializer
from rest_framework import permissions


class StoreViewset(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [permissions.IsAuthenticated]


class TransactionsViewset(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
