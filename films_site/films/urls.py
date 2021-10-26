from django.urls import path

from .views import *
from .get_data import get_day, month

urlpatterns =[
    path('genres/<int:genreid>', genres, name='genre'),
    path('', HomeFilms.as_view(), name='home'),
    path('main/', index),
    path('login/', user_login, name='login'),
    # path('register/', RegisterUser.as_view, name='register'),
    path('film/<int:pk>/', ViewFilm.as_view(), {'day': get_day, 'month': month}, name='view_film'),
    path('movie_theaters', get_theaters, name='theaters'),
    path('genre/<int:pk>/', show_genre, name='genre'),
]
