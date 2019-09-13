from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('movies/', views.movies_index, name='index'),
    path('movies/<int:movie_id>/', views.movies_detail, name='detail'),
    path('movies/create/', views.MovieCreate.as_view(), name='movies_create'), 
    path('movies/<int:pk>/update/', views.MovieUpdate.as_view(), name='movies_update'),
    path('movies/<int:pk>/delete/', views.MovieDelete.as_view(), name='movies_delete'),
    path('movies/<int:movie_id>/add_viewing/', views.add_viewing, name='add_viewing'),
    path('movies/<int:movie_id>/assoc_friend/<int:friend_id>/', views.assoc_friend, name='assoc_friend'),
    path('movies/<int:movie_id>/unassoc_friend/<int:friend_id>/', views.unassoc_friend, name='unassoc_friend'),
    path('movies/<int:movie_id>/add_photo/', views.add_photo, name='add_photo'),
    path('friends/', views.FriendList.as_view(), name='friends_index'),
    path('friends/<int:pk>/', views.FriendDetail.as_view(), name='friends_detail'), 
    path('friends/create/', views.FriendCreate.as_view(), name='friends_create'),
    path('friends/<int:pk>/update/', views.FriendUpdate.as_view(), name='friend_update'),
    path('friends/<int:pk>/delete/', views.FriendDelete.as_view(), name='friend_delete'),
]