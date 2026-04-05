import requests
import datetime as dt


# PARAMS
parameters = {
    'lat': 50.144125,
    'lng': 19.8817195,
    'formatted': 0,
}


time_now = dt.datetime.now().strftime("%H")



response = requests.get(f'https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()

sunrise = response.json()['results']['sunrise'][11:13]
sunset = response.json()['results']['sunset'][11:13]
print(sunrise)
print(sunset)
print(time_now)
