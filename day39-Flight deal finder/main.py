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


requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)

dotenv.load_dotenv()


# CONSTANTS
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")

GOOGLE_FLIGHT_API_ENDPOINT = os.getenv("GOOGLE_FLIGHT_API_ENDPOINT")

SHEETY_POST_ENDPOINT = os.getenv("SHEETY_POST_ENDPOINT")
SHEETY_PUT_ENDPOINT = os.getenv("SHEETY_PUT_ENDPOINT")

SERPY_API = os.getenv("SERPY_API")


tomorrow = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")
six_moths_from_now = (datetime.today() + timedelta(days=182)).strftime("%Y-%m-%d")



data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# pprint(sheet_data)
flight_search = FlightSearch()

flight = flight_search.search_flight(sheet_data[0]['iataCode'], tomorrow, six_moths_from_now)['best_flights'][0]
price = flight_search.search_flight(sheet_data[0]['iataCode'], tomorrow, six_moths_from_now)['best_flights'][0]['price']
# city = flight_search.search_flight(sheet_data[0]['iataCode'], tomorrow, six_moths_from_now)['best_flights'][0]['flights'][0]['arrival_airport']['name']

# print(f'{sheet_data[0]['city']}: {sheet_data[0]['iataCode']} {price}zł')


# for row in sheet_data:
#     i = flight_search.search_flight(row['iataCode'], tomorrow, six_moths_from_now)
#     pprint(i)
