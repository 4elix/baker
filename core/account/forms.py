from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите имя',
        'style': 'border: 2px solid #EAA636'
    }))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите пароль',
        'style': 'border: 2px solid #EAA636'
    }))
    password2 = forms.CharField(label='Подтверждения пароля', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Повторить пароль',
        'style': 'border: 2px solid #EAA636'
    }))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите имя',
        'style': 'border: 2px solid #EAA636'
    }))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите пароль',
        'style': 'border: 2px solid #EAA636'
    }))

    class Meta:
        model = User
        fields = ['username', 'password']
