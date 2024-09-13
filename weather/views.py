from django.shortcuts import render
import requests

# Create your views here.
def get_weather(request):
    if request.method == "POST":
        city = request.POST.get("city")
        api_key = '8562cb1c5fec04fe7befb01743674dda'
        base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(base_url)
        weather_data = response.json()

        if weather_data and weather_data.get('main'):
            temp_celsius = weather_data['main']['temp']
            temp_fahrenheit = temp_celsius * (9/5) + 32
            # fahrenheit_to_celsius_temp = (temp_fahrenheit - 32) * 5/9
        else:
            weather_data = None

        weather_data['main']['temp_fahrenheit'] = temp_fahrenheit
        # weather_data['main']['fahrenheit_to_celsius_temp'] = fahrenheit_to_celsius_temp

        context = {
            'city' : city,
            'weather_data' : weather_data
        }
        return render(request, template_name="weather/weather.html", context=context)
    return render(request, template_name="weather/weather.html")