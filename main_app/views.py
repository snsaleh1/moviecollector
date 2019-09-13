from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


import boto3
import uuid

from .forms import ViewingForm
from .models import Movie, Friend, Photo
# Add the following import

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'moviecollector-cns'

class MovieDelete(DeleteView):
    model = Movie
    success_url = '/movies/'

class MovieUpdate(UpdateView):
    model = Movie
    fields = ['year', 'rating', 'quote']

class MovieCreate(CreateView):
    model = Movie
    fields = ['name', 'year', 'rating', 'quote']
    success_url = '/movies/'


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
    friends_movie_doesnt_have = Friend.objects.exclude(id__in = movie.friends.all().values_list('id'))
    viewing_form = ViewingForm()
    return render(request, 'movies/detail.html', { 
        'movie': movie, 'viewing_form': viewing_form,
        'friends': friends_movie_doesnt_have
    })

def add_viewing(request, movie_id):
    form = ViewingForm(request.POST)
    # validate the form
    if form.is_valid():
    # don't save the form to the db until it
    # has the movie_id assigned
        new_viewing = form.save(commit=False)
        new_viewing.movie_id = movie_id
        new_viewing.save()
        return redirect('detail', movie_id=movie_id)

def assoc_friend(request, movie_id, friend_id):
    Movie.objects.get(id=movie_id).friends.add(friend_id)
    return redirect('detail', movie_id=movie_id)

def unassoc_friend(request, movie_id, friend_id):
    Movie.objects.get(id=movie_id).friends.remove(friend_id)
    return redirect('detail', movie_id=movie_id)


class FriendList(ListView):
    model = Friend

class FriendDetail(DetailView):
    model = Friend

class FriendCreate(CreateView):
    model = Friend
    fields = '__all__'
    success_url = '/friends/'


class FriendUpdate(UpdateView):
    model = Friend
    fields = ['name', 'bringing']
    success_url = '/friends/'


class FriendDelete(DeleteView):
    model = Friend
    success_url = '/friends/'

def add_photo(request, movie_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, movie_id=movie_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', movie_id=movie_id)