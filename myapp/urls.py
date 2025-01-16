# urls.py
from django.urls import path
from .views import BookListView, BookDetailView, borrow_book, return_book, user_borrow_history, list_users, create_book,home

urlpatterns = [
    path('', home, name='home'),  
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', create_book, name='create-book'),
    path('borrow/', borrow_book, name='borrow-book'),
    path('return/', return_book, name='return-book'),
    path('users/<int:user_id>/borrow-history/', user_borrow_history, name='user-borrow-history'),
    path('users/', list_users, name='list-users'),
]
