
from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255, unique=True)
    publisher = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    publication_date = models.DateField()
    number_of_copies_available = models.IntegerField()


    def __str__(self):
        return self.title

class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    borrowed_date = models.DateField()
    due_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
