from django.shortcuts import render
import json  # import json to use api - when we call an api, that request is being sent/receive in json format
import urllib.request

# Create your views here.


def index(request):

    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                     city+'&appid=fb22c554d7d46f25c8e0d5bbc371f6e3').read()

        # Store the current weather details of a city
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temperature": str(json_data['main']['temp']) + 'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }
    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})
