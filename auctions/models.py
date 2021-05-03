from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Watchlist(models.Model):
    users = models.IntegerField(null=True)
    listing  = models.IntegerField(null=True)

    def __int__(self):
        return self.listing

class Categories(models.Model):
    category = models.CharField(max_length=32)

    def __str__(self):
        return self.category

class Listings(models.Model):
    owner = models.CharField(max_length = 20)
    bidder = models.CharField(max_length = 20, null = True, default = "no bidders")
    title = models.CharField(max_length = 20)
    description = models.CharField(max_length = 200, null = True)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="posts", null = True)
    image = models.URLField(max_length = 1000, null = True)
    bid = models.PositiveIntegerField()
    close = models.BooleanField(default=False)

class Comments(models.Model):
    comment = models.CharField(max_length = 150)
    commenter = models.CharField(max_length = 20, default = "anonymous")
    listing = models.IntegerField(default=None, null = True)

    def __str__(self):
        return f"{self.comment}"
