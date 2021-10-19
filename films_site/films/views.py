from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import ListView

from films.models import Films


def genres(request, genreid):
    return HttpResponse(f'<h1>Фильм по категориям</h1><p>{genreid}</p>')


def home(request):
    return render(request, 'films/home_films_list.html',{'title': 'home_page'})


def index(request):
    return render(request, 'films/index.html')


def user_login(request):
    return render(request, 'films/login.html')


def show_film(request, film_id):
    return render(f'film with {film_id} id')

def get_theaters(request):
    return render(request, 'films/movie_theaters.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>страница не найдена</h1>')


class HomeFilms(ListView):
    model = Films
    template_name = 'films/home_films_list.html'
    context_object_name = 'films'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context
