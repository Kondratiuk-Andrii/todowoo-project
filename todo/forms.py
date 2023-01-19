from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Username",
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput(attrs={"class": "form-control"}))


class CreateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'memo', 'important')
