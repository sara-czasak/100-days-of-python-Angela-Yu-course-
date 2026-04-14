import requests
import dotenv
import os


dotenv.load_dotenv()

class DataManager:
    def __init__(self):
        self.header = {
    'Authorization': f'Bearer {os.getenv('SHEETY_AUTH_TOKEN')}',
        }
        self.get_endpoint = os.getenv('SHEETY_GET_ENDPOINT')
        self.post_endpoint = os.getenv('SHEETY_POST_ENDPOINT')


    def get_data(self):
        r = requests.get(self.get_endpoint, headers=self.header)
        r.raise_for_status()
        return r.json()['sheet1']