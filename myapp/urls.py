
# back_end/myapp/urls.py
from django.urls import path
from .views import home, BookListView, BookDetailView, BorrowCreateView, list_users, create_user, list_borrowed_books, borrow_book, return_book, create_book

urlpatterns = [
    path('', home, name='home'),  # Home URL
    path('users/', list_users, name='list-users'),
    path('users/create/', create_user, name='create-user'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', create_book, name='create-book'),
    path('borrowed/', list_borrowed_books, name='list-borrowed-books'),
    path('borrow/', BorrowCreateView.as_view(), name='borrow-create'),
    path('return/', return_book, name='return-book'),
]
