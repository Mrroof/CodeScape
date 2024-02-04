from django import forms 
from .models import Tip
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TipForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = ['title', 'content', 'category']


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']
