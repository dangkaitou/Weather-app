from django.shortcuts import render
import requests
import datetime
# Create your views here.

def index(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Ho Chi Minh'

    appid = 'c0e5aebcf653be75743536ca25c1667e'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q':city, 'appid':appid, 'units':'metric'}
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    C_temp = int(res['main']['temp'])
    F_temp = int(res['main']['temp'] * 9 / 5 + 32)

    day = datetime.date.today()
    # official city name from json
    city = res['name']

    return render(request, 'home/index.html', {'description': description, 'icon': icon, 'C_temp': C_temp, 'F_temp': F_temp, 'day': day, 'city': city})