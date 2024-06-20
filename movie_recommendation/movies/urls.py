from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('add/', views.add_movie, name='add_movie'),
    path('movies/<int:movie_id>/edit/', views.edit_movie, name='edit_movie'),
    path('movies/<int:movie_id>/delete/', views.delete_movie, name='delete_movie'),
]