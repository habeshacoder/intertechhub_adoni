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
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Remove is_admin if you want to manage it differently
        is_admin = validated_data.pop('is_admin', False)
        user = get_user_model().objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            **validated_data
        )
        user.is_admin = is_admin  # Optionally set is_admin
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        if email and password:
            user = get_user_model().objects.filter(email=email).first()
            if user and user.check_password(password):
                return attrs
        raise serializers.ValidationError("Invalid credentials")


class TokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()