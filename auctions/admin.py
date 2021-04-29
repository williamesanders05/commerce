from django.contrib import admin
from .models import Categories, User, Listings, Comments

# Register your models here.
admin.site.register(User)
admin.site.register(Categories)
admin.site.register(Listings)
admin.site.register(Comments)