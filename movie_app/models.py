
from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    duration = models.FloatField()
    directors = models.ForeignKey(Director, on_delete=models.CASCADE,
                                  null=True,related_name='movies')



    def __str__(self):
        return self.title

STAR_CHOICES = (
    (i, '* ' * i) for i in range(1, 6)
)


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                              related_name='reviews')
    stars = models.IntegerField(choices=STAR_CHOICES, default=5)

    def __str__(self):
        return self.text

