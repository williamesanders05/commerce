from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.createlisting, name="createlisting"),
    path("<int:listing_id", views.listing, name="listing"),
]
