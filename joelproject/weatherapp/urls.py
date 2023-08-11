# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('get_weather/<str:location>/', views.get_weather, name='get_weather'),
]