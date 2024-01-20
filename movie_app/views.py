from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Director, Review
from .serializers import MovieSerializer, DirectorSerializer, ReviewSerializer
from rest_framework import status



@api_view(['GET'])
def director_list(request):
    director = Director.objects.all()
    data = DirectorSerializer(director, many=True).data
    return Response(data=data)


@api_view(['GET'])
def director_detail(request, id):
    try:
        directors = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director does not exist'},
                        status=status.HTTP_404_NOT_FOUND)
    data = DirectorSerializer(directors).data
    return Response(data=data)

@api_view(['GET'])
def movie_list(request):
    movie = Movie.objects.all()
    data = MovieSerializer(movie, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movie_detail(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie does not exist'},
                        status=status.HTTP_404_NOT_FOUND)
    data = MovieSerializer(movie).data
    return Response(data=data)
@api_view(['GET'])
def review_list(request):
    review = Review.objects.all()
    data = ReviewSerializer(review, many=True).data
    return Response(data=data)


@api_view(['GET'])
def review_detail(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review does not exist'},
                        status=status.HTTP_404_NOT_FOUND)
    data = ReviewSerializer(reviews).data
    return Response(data=data)
