"""
View for book API
"""
import random
from rest_framework.decorators import api_view as API_VIEW
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from stage_2.models import Book
from stage_2.serializer import BookSerializer


# Get and Post Book View
@extend_schema(
    responses=BookSerializer(many=True),
    request=BookSerializer,
    description="Get all books."
)
@API_VIEW(["GET"])
def get_books(request):
    """Get all book view"""
    Books = Book.objects.all()
    serializer = BookSerializer(Books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@extend_schema(
    responses=BookSerializer,
    request=BookSerializer,
    description="Create a new book."
)
@API_VIEW(["POST"])
def post_book(request):
    """Post book view"""
    serializer=BookSerializer(data=request.data)
    print('------------------------')
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    responses=BookSerializer,
    description="Get a book by id."
)
@API_VIEW(['GET'])
def get_book(request, pk):
    """Get book by id  view"""
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({"detail":"Not Found"}, status=status.HTTP_404_NOT_FOUND)

    serializer=BookSerializer(book)
    return Response(serializer.data)

@extend_schema(
    responses=BookSerializer,
    request=BookSerializer,
    description="Update a book by id."
)
@API_VIEW(['PUT'])
def update_book(request,pk):
    """Update book by id  view"""
    try:
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Book.DoesNotExist:
        return Response({"detail":"Not Found"}, status=status.HTTP_404_NOT_FOUND)

@extend_schema(
    responses={204:"No Content"},
    description="Delete a book by id."
)
@API_VIEW(['DELETE'])
def delete_book(request,pk):
    """Delete book by id  view"""
    try:
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Book.DoesNotExist:
        return Response({"detail":"Not Found"}, status=status.HTTP_404_NOT_FOUND)


