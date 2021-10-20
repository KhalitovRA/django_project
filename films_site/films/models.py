from django.db import models


class Films(models.Model):
    en_title = models.CharField(max_length=150)
    ru_title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    duration_film = models.SmallIntegerField()
    film_score = models.FloatField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    trailer_link = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.ru_title

    def get_absolute_url(self):
        return reverse('view_film', kwargs={'film_id': self.pk})
