from rest_framework import serializers
from .models import User, Book, Borrow

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
class LibraryUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # or another model related to the library user
        fields = '__all__'  # or specify fields explicitly

class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = '__all__'
