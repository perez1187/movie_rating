import imp
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from .models import Movie, Rating
from rest_framework.response import Response
from .serializers import MovieSerializer, RatingSerializer

from django.contrib.auth.models import User

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
    authentication_classes = (TokenAuthentication,) # thx to this we know user

    ''' 
        create custom method
        1) decorator action with method
        
    '''
    @action(detail=True, methods=['POST']) # detail=True, - one specific movie, false - all movies
    def rate_movie(self, request, pk=None): # api/movies/{id}/rate_movie/
        if ('stars' in request.data) : # multiply conditions: and ('movie' in request.data)
            
            # we have access to pk
            movie = Movie.objects.get(id=pk)
            # print('Movie title', movie.title)
            user = request.user
            # user = User.objects.get(id=1) # temporary static user
            print('user', user)  # that will show AnonymousUser without atuhetication || user and usern.username in temporary it is the same
            stars=request.data['stars']

            '''
                api/movies/{id}/rate_movie/
                POST method
                if we have user and movie than update stars
                if we dont, create new
            '''

            try:
                rating= Rating.objects.get(user=user.id, movie=movie.id)
                rating.stars = stars
                rating.save()

                # we added serializer (but it works without) we just add more information to response JSON(front)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating updated', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                rating = Rating.objects.create(user=user, movie=movie, stars=stars) 
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating created', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)


        else:
            response = {
                'message': 'you need to provide stars'
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication,)


