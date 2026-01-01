from django.urls import path
from . import views

urlpatterns = [
    path("", views.movie_list, name="movie_list"),              # /movies/
    path("new/", views.movie_create, name="movie_create"),      # /movies/new/
    path("<int:pk>/", views.movie_detail, name="movie_detail"), # /movies/2/
    path("<int:pk>/edit/", views.movie_update, name="movie_update"),
    path("<int:pk>/delete/", views.movie_delete, name="movie_delete"),
]