import os
import requests
from dotenv import load_dotenv


load_dotenv()


# CONSTANTS
SHEETY_GET_ENDPOINT = os.getenv("SHEETY_GET_ENDPOINT")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")


class DataManager:
    def __init__(self):
        self.token = SHEETY_TOKEN
        self.destination_data ={}

    def get_destination_data(self):
        response = requests.get(SHEETY_GET_ENDPOINT, headers={"Authorization": f"Bearer {self.token}"})
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data