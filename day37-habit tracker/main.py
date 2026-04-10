import requests
import os
import dotenv


dotenv.load_dotenv()

PIXELA_AUTH = os.getenv("PIXELA_AUTH")
PIXELA_ENDPOINT = 'https://pixe.la/v1/users'

pixela_params = {
    'token': PIXELA_AUTH,
    'username':'StarWasp',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

response = requests.post(PIXELA_ENDPOINT, params=pixela_params)