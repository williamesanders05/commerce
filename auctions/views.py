
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import *


def index(request):
    return render(request, "auctions/index.html", {
        'listings': Listings.objects.filter(close = False),
        'name': 'Active Listings'
    })

@login_required(login_url= "login")
def createlisting(request):
    if request.method == "POST":
        listing = Listings(
            title = request.POST['title'],
            description = request.POST['description'],
            image = request.POST['image'],
            bid = request.POST['startingbid'],
            owner = request.user.username,
            categories=Categories.objects.get(category=request.POST["categories"])
        )

        listing.save()

        return HttpResponseRedirect(reverse('index'))

    return render(request, "auctions/createlisting.html", {
        'categories': Categories.objects.all()
    })

@login_required(login_url= "login")
def listing(request, listing_id):
    if request.method == "POST":
        Listings.objects.filter(id=listing_id).update(bid = request.POST['bid'])
        Listings.objects.filter(id=listing_id).update(bidder = request.user.username)
        return HttpResponseRedirect(reverse("listing", args=(listing_id,)))
    listing = Listings.objects.get(id=listing_id)
    comments = Comments.objects.filter(listing = listing_id)
    return render(request, "auctions/listing.html", {
        "listing": listing,
        'min_bid': listing.bid + 1,
        'comments': comments,
    })

@login_required(login_url= "login")
def categories(request):
    categories = Categories.objects.all()
    return render(request, "auctions/categories.html", {
        'categories': categories
    })

@login_required(login_url= "login")
def category(request, category_id):
    category = Listings.objects.filter(categories=category_id, close = False)
    return render(request, "auctions/category.html", {
        'listings': category,
    })

@login_required(login_url= "login")
def comment(request, listing_id):
    if request.method == "POST":
        comment = Comments(
            comment = request.POST["comment"],
            commenter = request.user.username,
            listing = listing_id
        )
        comment.save()
        return HttpResponseRedirect(reverse("listing", args=(listing_id,)))

@login_required(login_url= "login")
def close(request):
    if request.method == "POST":
        Listings.objects.filter(id=request.POST["listing_id"]).update(close = True)
        return HttpResponseRedirect(reverse('index'))
    return render(request, "auctions/close.html", {
        'listings': Listings.objects.filter(close = True),
        'name': "Closed Listings"
    })

@login_required(login_url= "login")
def closedlisting(request, listing_id):
    listing = Listings.objects.get(id=listing_id)
    return render(request, "auctions/closedlisting.html", {
        "listing": listing,
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
