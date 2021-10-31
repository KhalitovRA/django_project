from django.urls import path

from .views import *

urlpatterns =[
    path('', HomeFilms.as_view(), name='home'),
    path('main/', index, name='main'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('film/<int:pk>/', ViewFilm.as_view(), name='view_film'),
    path('movie_theaters', get_theaters, name='theaters'),
    path('genre/<int:pk>/', FilmsGenre.as_view(), name='genre'),
]

# TODO: решить проблему с фильмам по жанру