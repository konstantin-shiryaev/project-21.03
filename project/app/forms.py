from django import forms
from .models import *


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input', 'placeholder': 'Название поста'}
    ))
    content = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'textarea', 'placeholder': 'Описание поста'}
    ))
    slug = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input', 'placeholder': 'Slug поста'}
    ))

    class Meta:
        fields = ['title', 'content', 'slug']
        model = Post

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input', 'placeholder': 'Оставьте свой комментарий'}
    ))
    class Meta:
        fields = ['body']
        model = Comment

        