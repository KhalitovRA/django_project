from django.urls import path

from .views import *

urlpatterns =[
    path('', home, name='home'),
    path('main/', index),
    path('film/<int:pk>/', ViewFilms.as_view()),
]
