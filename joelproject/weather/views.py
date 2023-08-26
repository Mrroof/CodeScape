import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    url= 'http://api.weatherapi.com/v1/current.json?key=ef910f5466bc4a1d83e00203232608&q=London&aqi=no'
    city= 'London'

    r = requests.get(url.format(city))
    return render(request, 'weather/weather.html')