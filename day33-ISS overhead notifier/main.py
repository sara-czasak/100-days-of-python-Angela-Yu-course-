import requests
import datetime as dt
import smtplib
import os
from dotenv import load_dotenv
import time


load_dotenv()

# CONSTANTS
my_email = os.getenv('my_email')
app_password = os.getenv('app_password')


# Getting sunrise/sunset data
# PARAMS
parameters = {
    'lat': 50.144125,
    'lng': 19.8817195,
    'formatted': 0,
}

my_position = (parameters['lat'], parameters['lng'])

time_now = dt.datetime.now().strftime("%H")

response = requests.get(f'https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()

sunrise = int(response.json()['results']['sunrise'][11:13])
sunset = int(response.json()['results']['sunset'][11:13])


# Getting ISS data
response = requests.get('http://api.open-notify.org/iss-now.json')
response.raise_for_status()

data = response.json()
latitude = float(data['iss_position']['latitude'])
longitude = float(data['iss_position']['longitude'])
iss_position = (latitude, longitude)


def check_if_within_range(iss_pos):
    if 55 >= iss_pos[0] <= 65 and 14 >= iss_pos[1] <= 19:
        return True
    else:
        return False


def check_if_dark(time, sunrise, sunset):
    if time < sunrise and time > sunset:
        return True
    else:
        return False

while True:
    time.sleep(60)
    if check_if_within_range(iss_position) and check_if_dark(time_now, sunrise, sunset):
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=app_password)
            connection.sendmail(from_addr=my_email, to_addrs='sara.p.czasak.m@gmail.com', msg='Subject:ISS is overhead!\n\nLook up! You can see the ISS in the sky now!')
