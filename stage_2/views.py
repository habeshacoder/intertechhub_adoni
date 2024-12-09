"""
View for book API
"""
from rest_framework.decorators import api_view as API_VIEW, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema
from stage_2.models import Book
from stage_2.serializer import BookSerializer, LoginSerializer, TokenSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission
from .models import User


class IsAdmin(BasePermission):
    """Custom persmission to allow only admins to access to views"""
    def has_permission(self, request, view):
        return request.user and request.user.is_admin


class IsUser(BasePermission):
    """Custom permission to allow only users to access certain views"""
    def has_permission(self, request, view):
        return request.user and not request.user.is_admin

# Get and Post Book View
@extend_schema(
    request=UserSerializer,
    description="Create a new user.")
@API_VIEW(["POST"])
def signup(request):
    """Create a new user."""
    serializer = UserSerializer(data=request.data)
    try:
        if serializer.is_valid():
            try:
                user = serializer.save()
                token = RefreshToken.for_user(user)
                return Response({'refresh': str(token), 'access': str(token.access_token)}, status=status.HTTP_201_CREATED)
            except Exception as e:
                print("Error during user creation:", e)
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        else:
            print("Validation Errors:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        return Response({"error": str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@extend_schema(
    request=LoginSerializer,
    description="Login end point.")
@API_VIEW(["POST"])
def login(request):
    """Login a user and return JWT token."""
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user = User.objects.filter(email=email).first()
        if user and user.check_password(password):
            token = RefreshToken.for_user(user)
            return Response({'refresh': str(token), 'access': str(token.access_token)}, status=status.HTTP_200_OK)
        return Response({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get and Post Book View
@extend_schema(
    responses=BookSerializer(many=True),
    request=BookSerializer,
    description="Get all books.")
@API_VIEW(["GET"])
@permission_classes([IsAuthenticated, IsAdmin])
def get_books(request):
    """Get all book view"""
    Books = Book.objects.all()
    serializer = BookSerializer(Books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(
    responses=BookSerializer,
    request=BookSerializer,
    description="Create a new book.")
@API_VIEW(["POST"])
@permission_classes([IsAuthenticated, IsUser])
def post_book(request):
    """Post book view"""
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    responses=BookSerializer,
    description="Get a book by id.")
@API_VIEW(['GET'])
@permission_classes([IsAuthenticated])
def get_book(request, pk):
    """Get book by id  view"""
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({"detail": "Not Found"},
                        status=status.HTTP_404_NOT_FOUND)

    serializer = BookSerializer(book)
    return Response(serializer.data)


@extend_schema(
    responses=BookSerializer,
    request=BookSerializer,
    description="Update a book by id.")
@API_VIEW(['PUT'])
@permission_classes([IsAuthenticated, IsAdmin])
def update_book(request, pk):
    """Update book by id  view"""
    try:
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Book.DoesNotExist:
        return Response({"detail": "Not Found"},
                        status=status.HTTP_404_NOT_FOUND)


@extend_schema(
    responses={204: "No Content"},
    description="Delete a book by id.")
@API_VIEW(['DELETE'])
@permission_classes([IsAuthenticated, IsAdmin])
def delete_book(request, pk):
    """Delete book by id  view"""
    try:
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Book.DoesNotExist:
        return Response({"detail": "Not Found"},
                        status=status.HTTP_404_NOT_FOUND)


@extend_schema(
    responses=BookSerializer,
    description="Get all recommended books.")
@API_VIEW(['GET'])
@permission_classes([IsAuthenticated])
def get_recommended_books(request):
    """"Get all recommended books view"""
    book = Book.objects.order_by('?').first()
    if book:
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"detail": "No Recommended Books"},
                    status=status.HTTP_404_NOT_FOUND)


@extend_schema(
    responses=BookSerializer,
    description="Add a book to favorite by id",)
@API_VIEW(['PUT'])
@permission_classes([IsAuthenticated])
def favorite_book(request, pk):
    """"Add a book to favorite view"""

    try:
        book = Book.objects.get(pk=pk)
        book.isFavorite = True
        book.save()
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Book.DoesNotExist:
        return Response({"detail": "Not Found"},
                        status=status.HTTP_404_NOT_FOUND)
