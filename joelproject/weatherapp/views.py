from django.shortcuts import render
import requests
from django.conf import settings 
from django.http import JsonResponse
# Create your views here.
def get_weather(request):
    city = request.GET.get('city')
    api_key = settings.WEATHER_API_KEY
    url = f'https://api.weatherapi.com/v1/current.json?key={"2c5fb582e63f4767973123737230908"}&q={city}'
    
    
    response = requests.get(url)
    data = response.json()
   
   
    return JsonResponse(data)