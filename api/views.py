from rest_framework import viewsets, status
from rest_framework.decorators import action
from .models import Movie, Rating
from rest_framework.response import Response
from .serializers import MovieSerializer, RatingSerializer

class MovieViewSet(viewsets.ModelViewSet):
    '''
        A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
                    mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet)
    '''
    queryset = Movie.objects.all() # we can add fo example .order_by('')
    serializer_class = MovieSerializer

    ''' 
        create custom method
        1) decorator action with method
    '''
    @action(detail=True, methods=['POST']) # detail=True, - one specific movie, false - all movies
    def rate_movie(self, request, pk=None):
        response = {
            'message': 'its working'
        }
        return Response(response, status=status.HTTP_200_OK)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


