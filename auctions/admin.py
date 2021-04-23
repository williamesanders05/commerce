from django.contrib import admin
from .models import Categories, User, Listings, Watchlist, Comments

# Register your models here.
admin.site.register(User)
admin.site.register(Categories)
admin.site.register(Listings)
admin.site.register(Watchlist)
admin.site.register(Comments)