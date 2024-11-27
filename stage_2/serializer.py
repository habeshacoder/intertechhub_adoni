"""
Serializer for book
"""
from rest_framework import serializers

from stage_2.models import Book


class BookSerializer(serializers.ModelSerializer):
    """Serializer for book model"""
    class Meta:
        model = Book
        fields = '__all__'
        extra_kwargs = {
            'isFavorite': {'required': False, 'default': False},
        }
