from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE) # if we remove movie, we remove ratings
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)] # 1,2,3,4,5
    )

    class Meta:  # https://docs.djangoproject.com/en/4.1/ref/models/options/
        unique_together = (('user', 'movie'),) # Sets of field names that, taken together, must be unique
        index_together = (('user', 'movie'),) # Sets of field names that, taken together, are indexed

