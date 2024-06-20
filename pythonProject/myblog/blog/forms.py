from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.forms import ModelForm, TextInput, NumberInput, DateInput, TimeInput, formset_factory, Textarea

from django import forms

from .models import Post


class PostForms(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'text']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи',
            }),
            'content': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите краткое описание статьи',
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите текст статьи',
            }),
        }