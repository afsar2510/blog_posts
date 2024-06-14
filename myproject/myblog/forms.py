from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'style': 'width: 100%; padding:10px'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
