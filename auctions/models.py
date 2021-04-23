from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Categories(models.Model):
    category = models.CharField(max_length=32)

    def __str__(self):
        return self.category

class Comments(models.Model):
    comment = models.CharField(max_length = 150, null= True, blank= True)

    def __str__(self):
        return self.comment

class Listings(models.Model):
    owner = models.CharField(max_length = 20)
    bidder = models.CharField(max_length = 20, null = True, default = "no bidders")
    title = models.CharField(max_length = 20)
    description = models.CharField(max_length = 200, null = True)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="posts", null = True)
    image = models.URLField(max_length = 1000, null = True)
    bid = models.PositiveIntegerField()
    comments = models.ForeignKey(Comments, null= True, related_name = "posts", on_delete=models.CASCADE)

class Watchlist(models.Model):
    user = models.IntegerField()
    listings = models.ForeignKey("Listings", blank = True, related_name = "watchlist", on_delete=models.CASCADE)

    def __str__(self):
        return self.user
