from django.shortcuts import render
from library.models import Car, Movie, Game

# Create your views here.

def start(request):
    return render(request, 'index.html')

def show_cars(request):
    context = {"cars": Car.objects.all()}
    print(Car.objects.all())
    return render(request, "Cars.html", context=context)

def show_games(request):
    context = {'games': Game.objects.all()}

    return render(request, "Games.html", context=context)

def show_movies(request):
    context = {'movies': Movie.objects.all()}

    return render(request, 'Movies.html', context=context)