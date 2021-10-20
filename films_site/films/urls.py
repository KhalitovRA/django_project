from django.urls import path

from .views import *

urlpatterns =[
    path('genres/<int:genreid>', genres, name='genre'),
    path('', HomeFilms.as_view(), name='home'),
    path('main/', index),
    path('login/', user_login, name='login'),
    path('film/<int:pk>/', show_film, name='view_film'),
    path('movie_theaters', get_theaters, name='theaters'),
]
