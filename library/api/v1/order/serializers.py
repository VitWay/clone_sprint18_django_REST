from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'url', 'created_at', 'end_at', 'plated_end_at', 'user', 'book']