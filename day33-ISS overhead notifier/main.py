import requests
import os
import dotenv
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

# response = requests.get('http://api.open-notify.org/iss-now.json')
# response.raise_for_status()
#
# data = response.json()
# latitude = data['iss_position']['latitude']
# longitude = data['iss_position']['longitude']
# iss_position = (latitude, longitude)
# print(iss_position)