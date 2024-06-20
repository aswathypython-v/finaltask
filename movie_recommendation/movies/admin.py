from django.contrib import admin
from .models import Movie, Category, Review

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'genre', 'added_by')
    list_filter = ('release_date', 'genre')
    search_fields = ('title', 'actors')
    date_hierarchy = 'release_date'
    readonly_fields = ('added_by',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'user', 'rating')
    list_filter = ('movie', 'user', 'rating')
    search_fields = ('movie__title', 'user__username')


# Register your models here.
