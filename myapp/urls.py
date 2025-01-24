# urls.py
from django.urls import path
from .views import *

urlpatterns = [

    path('history/<int:id>', user_borrow_history, name='user-borrow-history'),
    # ************** crud table  users **************
    path('users', list_users, name='list-users'),
    path('users-create', create_library_user, name='create_library_user'),
    path('users-update', update_library_user, name='update_library_user'),
    path('users-delete/<int:id>', delete_library_user, name='delete_library_user'),
        # ************** crud table  books **************
    path('book/', list_books, name='list_books'),
    path('book-details', book_details, name='book_details'),
    path('book-create', create_book, name='create-book'),
    path('book-edit/<int:id>', edit_book, name='edit-book'),
    path('book-delete/<int:id>', delete_book, name='delete_book'),

    # ************** crud table  borrow **************
    path('borrow-create/', borrow_book, name='borrow-book'),
    path('borrowing-list/', borrows, name='return-book'),
    path('return/', return_book, name='return-book'),


    path('auth', auth, name='auth'),
    path('register', register, name='register'),



]
