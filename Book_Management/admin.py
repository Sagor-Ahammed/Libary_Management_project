from django.contrib import admin
from .models import Book, BorrowedBook
from Wishlist_Management.models import Wishlist
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'publisher', 'genre', 'language', 'publication_date', 'number_of_copies_available')
    list_filter = ('genre', 'language')
    search_fields = ('title', 'author', 'isbn')

admin.site.register(Book, BookAdmin)

admin.site.register(Wishlist)
admin.site.register(BorrowedBook)
