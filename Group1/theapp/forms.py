from django import forms

# Reordering Form and View


class PositionForm(forms.Form):
    position = forms.CharField()



from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Add this import

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')