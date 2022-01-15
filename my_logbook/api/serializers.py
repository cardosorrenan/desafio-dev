
from rest_framework import serializers
from app.models import Transaction, Store


class StoreSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Store
        fields = ('id', 'name', 'owner')


class TransactionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Transaction
        fields = ('id', 'value', 'datetime', 'store_id', 'type_id', 'file_origin_id')

