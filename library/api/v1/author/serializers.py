from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'url', 'name', 'surname', 'patronymic', 'author_books']
        extra_kwargs = {'author_books': {'required': False}}
