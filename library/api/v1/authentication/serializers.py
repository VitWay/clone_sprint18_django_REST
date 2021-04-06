from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'url', 'user_by_order', 'first_name', 'middle_name', 'last_name', 'email', 'password', 'role']
        extra_kwargs = {'user_by_order': {'required': False}}