from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .models import User, Book, Borrow, LibraryUser
from .serializers import UserSerializer, BookSerializer, BorrowSerializer, LibraryUserSerializer
from rest_framework import status
# back_end/myapp/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the homepage!")



class BorrowCreateView(CreateAPIView):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer

class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# User Views
@api_view(['GET'])
def list_users(request):
    """
    List all users.
    """
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

class BookListView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@api_view(['POST'])
def create_user(request):
    """
    Create a new user.
    """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Book Views
@api_view(['GET'])
def list_books(request):
    """
    List all books.
    """
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_book(request):
    """
    Create a new book.
    """
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Borrow Views
@api_view(['GET'])
def list_borrowed_books(request):
    """
    List all borrowed books.
    """
    borrowed_books = Borrow.objects.all()
    serializer = BorrowSerializer(borrowed_books, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def borrow_book(request):
    """
    Borrow a book.
    """
    serializer = BorrowSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def return_book(request):
    """
    Return a borrowed book.
    """
    try:
        borrow_id = request.data.get('borrow_id')
        borrow_instance = Borrow.objects.get(id=borrow_id)
        borrow_instance.return_date = request.data.get('return_date')
        borrow_instance.save()
        return Response({"message": "Book returned successfully"}, status=status.HTTP_200_OK)
    except Borrow.DoesNotExist:
        return Response({"error": "Borrow record not found"}, status=status.HTTP_404_NOT_FOUND)
