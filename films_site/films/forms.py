from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')