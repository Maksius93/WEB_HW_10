from django.db import models
from django.db import transaction
from pymongo import MongoClient
from django.conf import settings


# Create your models here.
class Author(models.Model):
    fullname = models.TextField(max_length=50)
    born_date = models.TextField(max_length=50)
    born_location = models.TextField(max_length=350)
    description = models.TextField(max_length=5000)


class Quote(models.Model):
    quote = models.TextField(max_length=3000)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.TextField(max_length=100)

