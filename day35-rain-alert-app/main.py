import requests
import os
import dotenv
from twilio.rest import Client


dotenv.load_dotenv()
API_KEY = os.getenv('API_KEY')
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
number = os.getenv("TWILIO_NUMBER")


parameters_hourly = {
    'lat': 50.064651,
    'lon': 19.944981,
    'appid': API_KEY,
    'cnt': 4
}



response = requests.get('https://pro.openweathermap.org/data/2.5/forecast', params=parameters_hourly)
response.raise_for_status()

def check_if_rain():
    for i in response.json()['list']:
        data = [i['weather'][0]['id'] for i in response.json()['list']]
        for j in data:
            if int(j) < 700:
                return True
            else:
                return False

if check_if_rain():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Bring an umbrella!",
        from_=number,
        to="+48692948897",
    )

