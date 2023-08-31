from django.shortcuts import render
import requests

def weather_view(request):
    api_key = '2d485dd751c5e1e23af0970ba2ce6bd3'

    if request.method == 'POST':
        user_input = request.POST.get('city')
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

        if weather_data.json()['cod'] == '404':
            weather = "No City Found"
            temp = ""
        else:
            weather = weather_data.json()['weather'][0]['main']
            temp = round(weather_data.json()['main']['temp'])
            city = user_input

        return render(request, 'weatherapp/weather.html', {'city': city, 'weather': weather, 'temp': temp})

    return render(request, 'weatherapp/weather.html', {'city': None})