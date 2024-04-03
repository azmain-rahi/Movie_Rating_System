

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Movie(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    rating = models.CharField(max_length=10)
    release_date = models.DateField()

    def __str__(self):
        return self.name

class Rating(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_ratings')
    rating = models.FloatField()

    def __str__(self):
        return f"{self.user.username} rated {self.movie.name} {self.rating}"