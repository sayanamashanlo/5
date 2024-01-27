from rest_framework import serializers
from .models import Movie, Director, Review


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

