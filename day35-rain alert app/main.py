import requests
import os
import dotenv

dotenv.load_dotenv()
API_KEY = os.getenv('API_KEY')


parameters = {
    "q": "Krakow",
    "appid": API_KEY
}


response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=parameters)


weather = response.json()['weather'][0]['main']

