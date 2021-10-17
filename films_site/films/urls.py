from django.urls import path

from .views import *

urlpatterns =[
    path('main/', index),
    path('', home),
    path('film/<str:film_name>/', get_film)
]