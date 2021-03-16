from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Categories(models.Model):
    category = models.CharField(max_length=32)

    def __str__(self):
        return self.category

class Listings(models.Model):
    owner = models.CharField(max_length = 20)
    title = models.CharField(max_length = 20)
    description = models.CharField(max_length = 100, null = True)
    categories = models.ForeignKey(Categories, related_name = "posts", null = True, on_delete = models.CASCADE)
    image = models.URLField(max_length = 1000, null = True)
    bid = models.PositiveIntegerField()

    def __str__(self):
        return self.title
