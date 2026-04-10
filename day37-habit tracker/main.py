import requests
import os
import dotenv


dotenv.load_dotenv()

PIXELA_AUTH = os.getenv("PIXELA_AUTH")
PIXELA_ENDPOINT = 'https://pixe.la/v1/users'


# REMEMBER username must be lowercase!
pixela_params = {
    'token': PIXELA_AUTH,
    'username':'starwasp7272',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

response = requests.post(PIXELA_ENDPOINT, json=pixela_params)
print(response.json())