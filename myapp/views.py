# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Book, Borrow, LibraryUser
from .serializers import BookSerializer, BorrowSerializer, LibraryUserSerializer
from rest_framework import status
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the homepage!")

# Book Views
class BookListView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@api_view(['POST'])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Borrow Views
@api_view(['POST'])
def borrow_book(request):
    serializer = BorrowSerializer(data=request.data)
    if serializer.is_valid():
        book = serializer.validated_data['book']
        if book.available_copies > 0:
            book.available_copies -= 1
            book.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": "No copies available"}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def return_book(request):
    try:
        borrow_id = request.data.get('borrow_id')
        borrow_instance = Borrow.objects.get(id=borrow_id)
        borrow_instance.return_date = request.data.get('return_date')
        borrow_instance.calculate_penalty()
        borrow_instance.save()

        # Update book copies
        borrow_instance.book.available_copies += 1
        borrow_instance.book.save()

        return Response({"message": "Book returned successfully", "penalty": borrow_instance.penalty}, status=status.HTTP_200_OK)
    except Borrow.DoesNotExist:
        return Response({"error": "Borrow record not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def user_borrow_history(request, user_id):
    borrows = Borrow.objects.filter(user__id=user_id).order_by('-borrow_date')
    serializer = BorrowSerializer(borrows, many=True)
    return Response(serializer.data)

# User Views
@api_view(['GET'])
def list_users(request):
    users = LibraryUser.objects.all()
    serializer = LibraryUserSerializer(users, many=True)
    return Response(serializer.data)