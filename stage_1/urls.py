from django.urls import path

from . import views

urlpatterns = [
    path('<str:option>', views.index),
]
