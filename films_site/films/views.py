from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from films.models import Films


def genres(request, genreid):
    return HttpResponse(f'<h1>Фильм по категориям</h1><p>{genreid}</p>')


def home(request):
    return render(request, 'films/home_films_list.html',{'title': 'home_page'})


def index(request):
    return render(request, 'films/index.html')


def user_login(request):
    return render(request, 'films/login.html')


def register(request):
    return render(request, 'films/register.html')


def show_genre(request, cat_id):
    return render(f'film with {cat_id} id')


class ViewFilm(DetailView):
    model = Films
    context_object_name = 'film_item'


def get_theaters(request):
    return render(request, 'films/movie_theaters.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>страница не найдена</h1>')


class HomeFilms(ListView):
    model = Films
    template_name = 'films/home_films_list.html'
    context_object_name = 'films'
    # success_url = reverse('home')


    def get_queryset(self):
        return Films.objects.filter(is_active=True)


class FilmsGenre(ListView):
    model = Films
    template_name = 'films/homes_films_list.html'
    context_object_name = 'films'

    def get_queryset(self):
        return Films.objects.filter(gen_id=self.kwargs['genre_id'], is_active=True)
