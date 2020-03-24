from django import forms

from .models import Post


class CategoryForm(forms.Form):
    text = forms.CharField(max_length=200)

    """
    class Meta:
        model = Category
        fields = ['text']
        labels = {'text': ''}
    """


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'category']
        labels = {'title': '', 'text': '', 'category': 'Category'}
        widgets = {
            'title': forms.TextInput(attrs={
                    'size': 80, 'placeholder': 'Title'
                    }),
            'text': forms.Textarea(attrs={'cols': 80}),
        }
