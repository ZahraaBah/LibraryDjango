from django import forms
from .models import Book, Borrow

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'publication_year', 'available_copies']

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = ['book', 'user']
