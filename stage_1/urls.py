from django.urls import path

from . import views

urlpatterns = [

    # handle the incoming request for / route
    path('', views.index),

    # handle the incoming request for /name route
    path('name', views.getName),

    # handle the incoming request for /hobby route
    path('hobby', views.getHobby),

    # handle the incoming request for /dream route
    path('dream', views.getDream),

    # handle the incoming request for any other route and respond notFound mesage with 404 status
    path('*', views.notFound),

]
