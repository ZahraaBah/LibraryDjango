from django.contrib import admin
from .models import Genre, Book, LibraryUser, Borrow

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'publication_year', 'available_copies')
    list_filter = ('genre', 'author')
    search_fields = ('title', 'author')

@admin.register(LibraryUser)
class LibraryUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'membership_date')

@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'borrow_date', 'return_date')
    list_filter = ('borrow_date', 'return_date')
