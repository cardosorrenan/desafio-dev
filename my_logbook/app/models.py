from django.db import models
from .utils import TransactionsActions, TransactionsSignals


# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=255, unique=True)
    owner = models.CharField(max_length=255)


class TransactionType(models.Model):
    type_num = models.IntegerField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    action = models.CharField(max_length=255, choices=TransactionsActions.choices())
    signal = models.CharField(max_length=1, choices=TransactionsSignals.choices())


class Transactions(models.Model):
    type = models.ForeignKey(TransactionType, on_delete=models.PROTECT)
    store = models.ForeignKey(Store, on_delete=models.PROTECT)
    timestamp = models.DateTimeField()
    value = models.CharField(max_length=255)
    cpf = models.CharField(max_length=255)
    card = models.CharField(max_length=255)
