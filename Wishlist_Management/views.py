from django.shortcuts import render,redirect

from Book_Management.views import BorrowedBook
from .models import Book, Wishlist
# Create your views here.

def add_to_wishlist(request, isbn):
    user = request.user
    book = Book.objects.get(isbn=isbn)
    wishlist = Wishlist.objects.create(user=user, book=book)
    return redirect('view_wishlist')

def remove_from_wishlist(request, isbn):
    user = request.user
    book = Book.objects.get(isbn=isbn)
    wishlist = Wishlist.objects.filter(user=user, book=book)
    wishlist.delete()
    return redirect('view_wishlist')

def view_wishlist(request):
    user = request.user
    wishlist = Wishlist.objects.filter(user=user)
    borrowed_books = BorrowedBook.objects.filter(user=request.user)
    borrowed_books_isbn_list = [book.book.isbn for book in borrowed_books]
    print(borrowed_books_isbn_list)
    return render(request, 'wishlist.html', context={'wishlist': wishlist, 'length_wishlist': len(wishlist), 'borrowed_books': borrowed_books_isbn_list})
