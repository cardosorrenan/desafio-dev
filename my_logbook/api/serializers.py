
from rest_framework import serializers
from app.models import FileOrigin, Store, Transaction
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.fields import SerializerMethodField


class FileOriginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FileOrigin
        fields = ('filename', 'content_type', 'size', 'entries', 'created_at', 'updated_at')


class StoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Store
        fields = ('id', 'name', 'owner')


class StoreTotalValuesSerializer(serializers.HyperlinkedModelSerializer):
    total_values = SerializerMethodField()

    def get_total_values(self, obj):
        return obj.total_values()['value__sum']

    class Meta:
        model = Store
        fields = ('id', 'total_values')


class TransactionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Transaction
        fields = ('id', 'value', 'datetime', 'store_id', 'type_id', 'file_origin_id')

