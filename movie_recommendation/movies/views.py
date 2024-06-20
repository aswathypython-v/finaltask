from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Movie, Review
from .forms import MovieForm, ReviewForm, CategoryFilterForm

def movie_list(request):
    movies = Movie.objects.all()
    form = CategoryFilterForm(request.GET)

    if 'q' in request.GET:
        query = request.GET['q']
        movies = movies.filter(title__icontains=query)

    if form.is_valid() and form.cleaned_data['category']:
        movies = movies.filter(genre=form.cleaned_data['category'])

    return render(request, 'movies/movie_list.html', {'movies': movies, 'form': form})




def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.save()
            return redirect('movie_detail', movie_id=movie.id)
    else:
        review_form = ReviewForm()

    return render(request, 'movies/movie_detail.html', {'movie': movie, 'review_form': review_form})


@login_required
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.added_by = request.user
            movie.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movies/add_movie.html', {'form': form})

@login_required
def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.user != movie.added_by:
        return HttpResponseForbidden("You are not allowed to edit this movie.")
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_detail', movie_id=movie_id)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/edit_movie.html', {'form': form, 'movie': movie})

@login_required
def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.user != movie.added_by:
        return HttpResponseForbidden("You are not allowed to delete this movie.")
    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')
    return render(request, 'movies/movie_confirm_delete.html', {'movie': movie})

