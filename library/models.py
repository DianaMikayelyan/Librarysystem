from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to='books/')
    cover_image = models.ImageField(upload_to='covers/', null=True, blank=True)
    digital_file = models.FileField(upload_to='book_files/', null=True, blank=True)
    read_link = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.title


class UserActivity(models.Model):
    ACTIVITY_CHOICES = [
        ('read','Read'),
        ('borrow','Borrow'),
    ]

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=10, choices=ACTIVITY_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f"{self.user.username} {self.activity_type} {self.book.title} on {self.timestamp}"

    
class Loan(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    loan_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.book.title} borrowed by {self.user.username}'



class BorrowRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_at = models.DateTimeField()
    return_by = models.DateTimeField()

    def __str__(self):
        return f'{self.user.username} borrowed {self.book.title}'
