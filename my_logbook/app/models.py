from django.db import models
from .utils import TransactionsActions, TransactionsSignals


# Create your models here.
class FileOrigin(models.Model):
    filename = models.CharField(max_length=255)
    content_type = models.CharField(max_length=255)
    size = models.FloatField()
    entries = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Store(models.Model):
    name = models.CharField(max_length=19, unique=True)
    owner = models.CharField(max_length=14)


class TransactionType(models.Model):
    type_num = models.IntegerField(unique=True)
    description = models.CharField(max_length=255)
    action = models.CharField(max_length=10, choices=TransactionsActions.choices())
    signal = models.CharField(max_length=1, choices=TransactionsSignals.choices())


class Transaction(models.Model):
    file_origin = models.ForeignKey(FileOrigin, related_name='file', on_delete=models.PROTECT)
    type = models.ForeignKey(TransactionType, related_name='type', on_delete=models.PROTECT)
    store = models.ForeignKey(Store, related_name='store', on_delete=models.PROTECT)
    datetime = models.DateTimeField()
    value = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    