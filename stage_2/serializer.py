"""
Serializer for book
"""
from rest_framework import serializers

from stage_2.models import Book
from django.contrib.auth import get_user_model

class BookSerializer(serializers.ModelSerializer):
    """Serializer for book model"""
    class Meta:
        model = Book
        fields = '__all__'
        extra_kwargs = {
            'isFavorite': {'required': False, 'default': False},
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'is_admin']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()