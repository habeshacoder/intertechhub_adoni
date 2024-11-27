"""
Urls for stage_2 app
"""
from django.urls import path

from .views import (
    get_books,
    post_book,
    get_book,
    update_book,
    delete_book,
)


app_name = 'stage_2'

urlpatterns = [
    path('books', get_books, name='get_books', ),
    path('book', post_book, name='post_book', ),
    path('book/<int:pk>', get_book, name='get_book', ),
    path('book/update/<int:pk>', update_book, name='update_book',),
    path('book/delete/<int:pk>', delete_book, name='delete_book',),
]
