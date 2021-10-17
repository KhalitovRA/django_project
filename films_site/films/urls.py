from django.urls import path

from .views import *

urlpatterns =[
    path('main/', index),
    path('film/<int:pk>/', ViewFilms.as_view()),
]