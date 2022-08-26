from rest_framework import viewsets
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all() # we can add fo example .order_by('')
    serializer_class = MovieSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


