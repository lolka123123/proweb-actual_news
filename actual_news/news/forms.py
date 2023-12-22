from django import forms

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from . import models

class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))

    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))


class AuthenticatedCommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Написать комментарий',
                'cols': '50',
                'rows': '5',
                'style': 'font-size: 20px; padding: 5px;',
            })
        }

class UnauthenticatedCommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['name', 'text']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Написать имя',
                'style': 'font-size: 20px; outline: none; padding: 5px;',
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Написать комментарий',
                'cols': '50',
                'rows': '5',
                'style': 'font-size: 20px; padding: 5px;',
            })
        }




class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['image', 'description']
        widgets = {
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'cols': '30',
                'rows': '10'
            })
        }