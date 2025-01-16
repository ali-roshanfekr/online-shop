from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'phone', 'email', 'password1', 'password2')


class LogInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'name': 'username', 'placeholder': 'username', 'class': 'input-xlarge'
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'name': 'password', 'placeholder': 'password', 'class': 'input-xlarge'
    }))


class NewPassWordForm(forms.Form):
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'name': 'password1', 'placeholder': 'password', 'class': 'input-xlarge'
    }))

    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'name': 'password2', 'placeholder': 'password', 'class': 'input-xlarge'
    }))
