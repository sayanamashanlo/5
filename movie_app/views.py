from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from .models import Director, Movie, Review
from .serializers import (ReviewSerializer, DirectorSerializer, MovieSerializer,
                          DirectorValidateSerializer, MovieValidateSerializer, ReviewValidateSerializer)
from rest_framework import status


class DirectorListCreateAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    pagination_class = PageNumberPagination


# @api_view(['GET', 'POST'])
# def director_list(request):
#     if request.method == 'GET':
#         directors = Director.objects.all()
#         serializer = DirectorSerializer(directors, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = DirectorValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST,
#                             data={'errors': serializer.errors})
#         name = serializer.validated_data.get('name')
#
#         director = Director.objects.create(name=name)
#         return Response(data={'director_id': director.id}, status=status.HTTP_201_CREATED)


class DirectorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'


# @api_view(['GET', 'PUT', 'DELETE'])
# def director_detail(request, id):
#     director = Director.objects.get(id=id)
#     if request.method == 'GET':
#         data = {'name': director.name}
#         return Response(data=data)
#     elif request.method == 'DELETE':
#         director.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         serializer = DirectorValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         director.name = request.data.get('name')
#         director.save()
#         return Response(data={'director_id': director.id}, status=status.HTTP_201_CREATED)


class MovieListCreateAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination

    def post(self, request, *args, **kwargs):
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        title = request.data.get('title')
        genres = request.data.get('genres')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')

        movie = Movie.objects.create(title=title, description=description,
                                     duration=duration, director_id=director_id)
        movie.genres.set(genres)
        movie.save()
        return Response(data={'movie_id': movie.id}, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         data = MovieSerializer(movies, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializer = MovieValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST,
#                             data={'errors': serializer.errors})
#         title = serializer.validated_data.get('title')
#         genres = serializer.validated_data.get('genres')
#         description = serializer.validated_data.get('description')
#         duration = serializer.validated_data.get('duration')
#         director_id = serializer.validated_data.get('director_id')
#
#         movie = Movie.objects.create(title=title, description=description,
#                                      duration=duration, director_id=director_id)
#         movie.genres.set(genres)
#         movie.save()
#         return Response(data={'movie_id': movie.id}, status=status.HTTP_201_CREATED)

class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'


# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request, id):
#     movie = Movie.objects.get(id=id)
#     if request.method == 'GET':
#         data = {'movie': {
#             'title': movie.title,
#             'description': movie.description,
#             'duration': movie.duration,
#             'director': movie.director.name,
#         }}
#         return Response(data=data)
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         serializer = MovieValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         movie.title = request.data.get('title')
#         movie.description = request.data.get('description')
#         movie.duration = request.data.get('duration')
#         movie.director_id = request.data.get('director_id')
#         movie.save()
#         return Response(data={'movie_id': movie.id}, status=status.HTTP_201_CREATED)


class ReviewListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination


# @api_view(['GET', 'POST'])
# def review_list(request):
#     if request.method == 'GET':
#         reviews = Review.objects\
#             .select_related('movie').all()
#         serializer = ReviewSerializer(reviews, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ReviewValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST,
#                             data={'errors': serializer.errors})
#
#         text = serializer.validated_data.get('text')
#         movie_id = serializer.validated_data.get('movie_id')
#         stars = serializer.validated_data.get('stars')
#
#         review = Review.objects.create(text=text, movie_id=movie_id, stars=stars)
#         return Response(data={'review_id': review.id}, status=status.HTTP_201_CREATED)


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'


# @api_view(['GET', 'PUT', 'DELETE'])
# def review_detail(request, id):
#     review = Review.objects.get(id=id)
#     if request.method == 'GET':
#         data = {'review': {
#             'text': review.text,
#             'movie': review.movie.title,
#         }}
#         return Response(data=data)
#     elif request.method == 'DELETE':
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         serializer = ReviewValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#
#         review.text = request.data.get('text')
#         review.movie_id = request.data.get('movie_id')
#         review.stars = request.data.get('stars')
#
#         review.save()
#         return Response(data={'review_id': review.id}, status=status.HTTP_201_CREATED)