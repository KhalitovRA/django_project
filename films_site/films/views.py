from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import DetailView

from films.models import Films


def home(request):
    return render(request, 'films/home_films_list.html')


def index(request):
    return render(request, 'films/index.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>страница не найдена</h1>')


class ViewFilms(DetailView):
    model = Films
    # context_object_name = ''