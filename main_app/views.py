from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Movie
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Add the following import
from django.http import HttpResponse

class MovieDelete(DeleteView):
  model = Movie
  success_url = '/movies/'

class MovieUpdate(UpdateView):
  model = Movie
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['year', 'rating', 'quote']

class MovieCreate(CreateView):
  model = Movie
  fields = '__all__'

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def movies_index(request):
  movies = Movie.objects.all()
  return render(request, 'movies/index.html', { 'movies': movies })

def movies_detail(request, movie_id):
  movie = Movie.objects.get(id=movie_id)
  return render(request, 'movies/detail.html', { 'movie': movie })

