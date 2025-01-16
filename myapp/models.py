# models.py
from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    publication_year = models.IntegerField()
    available_copies = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class LibraryUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(LibraryUser, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    penalty = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.user.user.username} borrowed {self.book.title}"

    def calculate_penalty(self):
        if self.return_date and self.return_date > self.borrow_date:
            overdue_days = (self.return_date - self.borrow_date).days - 14  # 14-day loan period
            if overdue_days > 0:
                self.penalty = overdue_days * 0.50  # 0.50 units per day overdue
            else:
                self.penalty = 0.0