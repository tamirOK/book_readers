from django.db import models

# Create your models here.

from rest_framework import serializers


class Book(models.Model):

    GENRES_LIST = [
        ("Crime", "Crime"),
        ("Drama", "Drama"),
        ("Fantasy", "Fantasy"),
    ]

    name = models.CharField(max_length=100)
    genre = models.CharField(choices=GENRES_LIST, max_length=100)
    publish_date = models.DateField()
    pages = models.PositiveSmallIntegerField()
    reader = models.ForeignKey('Reader', null=True, on_delete=models.SET_NULL, related_name='books')

    def __str__(self):
        return f"{self.name}[{self.id}]"


class Reader(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
