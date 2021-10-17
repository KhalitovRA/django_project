from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return HttpResponse('Страница приложения фильмов')


def home(request):
    return HttpResponse('Это будет основная страница')


def get_film(request, film_name):
    return HttpResponse('')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>страница не найдена</h1>')