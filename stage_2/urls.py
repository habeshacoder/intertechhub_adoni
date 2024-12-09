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
    get_recommended_books,
    favorite_book,
    signup,
    login,
)


app_name = 'stage_2'

urlpatterns = [
    path('book', post_book, name='post_book', ),
    path('book/all', get_books, name='get_books', ),
    path('book/<int:pk>', get_book, name='get_book', ),
    path('book/update/<int:pk>', update_book, name='update_book',),
    path('book/delete/<int:pk>', delete_book, name='delete_book',),
    path('book/recommended',
         get_recommended_books, name='get_recommended_books',),
    path('book/favorite/<int:pk>', favorite_book, name='favorite_book',),

    path('signup', signup, name='signup',),
    path('signin', login, name='login',),

]
