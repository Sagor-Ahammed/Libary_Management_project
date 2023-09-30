from django.db import models
from Book_Management.models import Book
# Create your models here.
class Wishlist(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"