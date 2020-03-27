from django import forms

from .models import Post, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['text']
        labels = {'text': ''}
        help_texts = {'text': 'Insert the name for a new category'}


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'category']
        labels = {'title': '', 'text': '', 'category': 'Category'}
        widgets = {
            'title': forms.TextInput(attrs={
                    'size': 80, 'placeholder': 'Title'
                    }),
            'text': forms.Textarea(attrs={'cols': 80})
        }
