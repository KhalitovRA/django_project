from django import template
from django.db.models import Count, F

from films.models import Genres


register = template.Library()


@register.simple_tag()
def get_list_genres():
    return Genres.objects.all()


@register.inclusion_tag('films/home_films_list.html')
def show_genres(arg1='Hello', arg2='World'):
    genres = Genres.objects.annotate(cnt=Count('news', filter=F('films__is_active'))).filter(cnt__gt=0)
    return {"genres": genres, "arg1": arg1, "arg2": arg2}
