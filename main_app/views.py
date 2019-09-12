from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Movie
from .forms import ViewingForm
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
  viewing_form = ViewingForm()
  return render(request, 'movies/detail.html', { 'movie': movie, 'viewing_form': viewing_form })

def add_viewing(request, cat_id):
    form = ViewingForm(request.POST)
    # validate the form
    if form.is_valid():
    # don't save the form to the db until it
    # has the movie_id assigned
        new_viewing = form.save(commit=False)
        new_viewing.movie_id = movie_id
        new_viewing.save()
        return redirect('detail', movie_id=movie_id)