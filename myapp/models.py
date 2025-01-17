from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=90)  # Reduced max_length for better MySQL compatibility
    author = models.CharField(max_length=90)
    genre = models.CharField(max_length=10)
    publication_year = models.IntegerField()
    available_copies = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Users(models.Model):
    username = models.CharField(max_length=90, unique=True)  # Adding unique constraint for uniqueness
    password = models.CharField(max_length=90)   
    email = models.CharField(unique=True,max_length=40,default="22000@gmail.com")  # Adding unique constraint for uniqueness
    status = models.CharField(max_length=10,default="active")
    role = models.CharField(max_length=10,default="user")

    def __str__(self):
        return self.username



class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    penalty = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"

    def calculate_penalty(self):
        if self.return_date and self.return_date > self.borrow_date:
            overdue_days = (self.return_date - self.borrow_date).days - 14  # Assuming 14 days for borrowing
            if overdue_days > 0:
                self.penalty = overdue_days * 0.50  # Penalty of 0.50 units per day
            else:
                self.penalty = 0.0
