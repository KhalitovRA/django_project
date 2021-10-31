from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout

from .models import Films
from .get_data_info import get_four_days
from .utils import DataMixin
from .forms import *


def genres(request, genreid):
    return HttpResponse(f'<h1>Фильм по категориям</h1><p>{genreid}</p>')


def home(request):
    return render(request, 'films/home_films_list.html',{'title': 'home_page'})


def index(request):
    return render(request, 'films/index.html')


def user_logout(request):
    logout(request)
    return redirect('login')


def register(request):
    return render(request, 'films/register.html')


def show_genre(request, cat_id):
    return render(f'film with {cat_id} id')


class ViewFilm(DetailView):
    model = Films
    context_object_name = 'film_item'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = get_four_days()
        return context


def get_theaters(request):
    return render(request, 'films/movie_theaters.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>страница не найдена</h1>')


class HomeFilms(ListView):
    model = Films
    template_name = 'films/home_films_list.html'
    context_object_name = 'films'
    paginate_by = 1
    # success_url = reverse('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Films.objects.filter(is_active=True)


class FilmsGenre(ListView):
    model = Films
    template_name = 'films/homes_films_list.html'
    context_object_name = 'films'

    def get_queryset(self):
        return Films.objects.filter(gen_id=self.kwargs['genre_id'], is_active=True)


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'films/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'films/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('home')
