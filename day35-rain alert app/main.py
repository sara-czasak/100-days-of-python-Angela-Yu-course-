import requests
import os
import dotenv

dotenv.load_dotenv()
API_KEY = os.getenv('API_KEY')


parameters_hourly = {
    'lat': 50.064651,
    'lon': 19.944981,
    'appid': API_KEY,
}

response = requests.get('https://pro.openweathermap.org/data/2.5/forecast', params=parameters_hourly)

def check_if_rain():
    for i in response.json()['list']:
        data = [i['weather'][0]['main'] for i in response.json()['list']][:12]
        if 'Rain' in data:
            return True
        else:
            return False

if check_if_rain():
    print('Bring an umbrella')