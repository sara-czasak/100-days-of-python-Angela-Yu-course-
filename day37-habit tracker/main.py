import requests
import os
import dotenv
import datetime as dt


today = (dt.date.today()).strftime("%Y%m%d")
print(today)



dotenv.load_dotenv()

PIXELA_AUTH = os.getenv("PIXELA_AUTH")
PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")
PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
GRAPH_ID = 'graph1'

# REMEMBER username must be lowercase!
pixela_params = {
    'token': PIXELA_AUTH,
    'username': PIXELA_USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(PIXELA_ENDPOINT, json=pixela_params)
# print(response.json())

# GRAPH_ENDPOINT = f'{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs'
#
# graph_config = {
#     'id': 'graph1',
#     'name': 'Beading Tracker',
#     'unit': 'item',
#     'type': 'int',
#     'color': 'ajisai'
# }
#
request_header = {
    'X-USER-TOKEN': PIXELA_AUTH,
}
#
# response = requests.post(GRAPH_ENDPOINT, json=graph_config, headers=request_header)
# print(response.text)

# Posting a pixel to graph

pixel_config = {
    'date': today,
    'quantity': "5"
}

PIXEL_ENDPOINT = f'{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}'

response = requests.post(PIXEL_ENDPOINT, headers=request_header, json=pixel_config)
print(response.text)