from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'url', 'name', 'description', 'count', 'authors']
        extra_kwargs = {'authors': {'required': False}}
