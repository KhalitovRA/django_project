from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Страница приложения фильмов')


def home(request):
    return HttpResponse('Это будет основная страница')
