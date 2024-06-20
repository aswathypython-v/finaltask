from django import forms
from .models import Movie
from .models import Category
from .models import Review


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'poster', 'description', 'release_date', 'actors', 'genre', 'youtube_trailer', 'added_by']

class CategoryFilterForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='All Categories', required=False)

# forms.py

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating','user']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 0, 'max': 5})
        }

