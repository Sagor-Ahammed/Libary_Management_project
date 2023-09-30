from django.urls import path
from .views import Home, view_books, view_books_search, signup_view, login_view, logout_view, borrow_book, return_book, view_borrowed_books, extra_fines, get_notifications
from Wishlist_Management.views import add_to_wishlist,remove_from_wishlist,view_wishlist
urlpatterns = [
    path('', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/',Home, name='home'),
    path('view_books/', view_books, name='view_books'),
    path('view_books/search/<str:search_term>/', view_books_search, name='view_books_search'),
    path('add_to_wishlist/<str:isbn>/', add_to_wishlist, name='add_to_wishlist'),
    path('remove_from_wishlist/<str:isbn>/', remove_from_wishlist, name='remove_from_wishlist'),
    path('view_wishlist/', view_wishlist, name='view_wishlist'),
    path('borrow_book/<str:isbn>/', borrow_book, name='borrow_book'),
    path('return_book/<str:isbn>/', return_book, name='return_book'),
    path('view_borrowed_books/', view_borrowed_books, name='view_borrowed_books'),
    path('extra_fines/', extra_fines, name='extra_fines'),
    path('notifications/', get_notifications, name='get_notifications')
]