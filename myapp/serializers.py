from rest_framework import serializers
from .models import Users, Book, Borrow

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
 
class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = '__all__'
