# from for add category and category

from django import forms
from .models import Category, Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'price',
            'cover',
            'photo_author',
            'pages',
            'rental_price_day',
            'rental_period',
            'status',
            'category',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'cover': forms.FileInput(attrs={'class': 'form-control'}),
            'photo_author': forms.FileInput(attrs={'class': 'form-control'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'rental_price_day': forms.NumberInput(attrs={'class': 'form-control'}),
            'rental_period': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=100)

    class Meta:
        model = Category
        fields = ['name']