"""
Serializer for book
"""
from rest_framework import serializers
from .models import User
from stage_2.models import Book

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
        model = User
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        is_admin = validated_data.get('is_admin', False)
        validated_data.pop('is_admin', None)
        user = User.objects.create_user(is_admin=is_admin, **validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class TokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()