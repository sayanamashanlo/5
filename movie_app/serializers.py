from rest_framework import serializers
from .models import Movie, Director, Review
from rest_framework.exceptions import ValidationError

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title description duration directors'.split()


class DirectorSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)
    movies_count = serializers.SerializerMethodField()
    class Meta:
        model = Director
        fields = 'id', 'name', 'movies', 'movies_count'

    def get_movies_count(self, name):
        return name.movies.count()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie

        def get_rating(self, movie):
            average_rating = sum([star.stars for star in movie.reviews.all()]) / len(
                [star.stars for star in movie.reviews.all()])
            return average_rating

        fields = '__all__'

class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=1, max_length=100)


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=100)
    genres = serializers.CharField(min_length=1)
    description =serializers.CharField(required=False)
    duration = serializers.IntegerField()
    director_id = serializers.IntegerField()

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError('Director not found!')
        return director_id

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=1, max_length=100)
    movi_id = serializers.IntegerField()
    stars = serializers.IntegerField(min_value=1, max_value=5)

    def validate_movie_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise ValidationError('Movie not found!')
        return movie_id