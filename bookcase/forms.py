from django import forms
from .models import Author, Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'description','cover' ]

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'second_name', 'face', 'biography']

# class ReviewForm(forms.ModelForm):

#     class Meta:
#         model = Review
#         fields = ('author', 'text',)