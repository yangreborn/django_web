from django.urls import path
from .views import customuser, post, book

urlpatterns = [
    path('users/', customuser.user_list, name='book-create-list'),
    path('posts/', post.post_list, name='post-create-list'),
    path('books/', book.book_list, name='book-create-list'),
    path('books/<int:id>', book.book_details, name='book-detail'),
]
