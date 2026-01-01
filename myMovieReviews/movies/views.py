from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm

def movie_list(request):
    movies = Movie.objects.order_by("-year")
    return render(request, "movie_list.html", {"movies": movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, "movie_detail.html", {"movie": movie})

def movie_create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movie_list")
    else:
        form = MovieForm()

    return render(request, "movie_form.html", {"form": form})


def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == "POST": #post하면
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect("movie_detail", pk=pk)
    else:
        form = MovieForm(instance=movie)

    return render(request, "movie_form.html", {"form": form})

def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        movie.delete()
        return redirect("movie_list")
    return redirect("movie_detail", pk=pk)

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, "movie_detail.html", {"movie": movie})