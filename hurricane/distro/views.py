from django.shortcuts import render
from allauth.account.views import SignupView
from allauth.account.views import LoginView



class CustomSignupView(SignupView):
    template_name = 'registration/registration_form.html'



class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    
# Create your views here.
