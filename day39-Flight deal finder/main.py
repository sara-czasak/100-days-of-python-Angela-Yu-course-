from dataclasses import *
from flight_search import *
from flight_data import *
from notification_manager import *
from data_manager import *
import requests
import os
import dotenv
from pprint import pprint
import requests_cache
from datetime import datetime, timedelta


requests_cache.install_cache()
dotenv.load_dotenv()


# CONSTANTS
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
GOOGLE_FLIGHT_API_ENDPOINT = os.getenv("GOOGLE_FLIGHT_API_ENDPOINT")

SHEETY_POST_ENDPOINT = os.getenv("SHEETY_POST_ENDPOINT")
SHEETY_PUT_ENDPOINT = os.getenv("SHEETY_PUT_ENDPOINT")
tomorrow = datetime.today() + timedelta(days=1)
six_moths_from_now = datetime.today() + timedelta(days=182)


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
pprint(sheet_data)