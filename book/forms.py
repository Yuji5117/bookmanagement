from django import forms
from .models import Book, Category


class SearchForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset = Category.objects, required=False
    )