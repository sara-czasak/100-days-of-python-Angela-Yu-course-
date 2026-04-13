import requests
import datetime as dt
import os
import dotenv


dotenv.load_dotenv()

WORKOUT_API_KEY = os.getenv('WORKOUT_API')
WORKOUT_APP_ID = os.getenv('WORKOUT_APP_ID')
SHEETY_POST_ENDPOINT = os.getenv('SHEETY_POST_ENDPOINT')
SHEETY_TOKEN = os.getenv('SHEETY_TOKEN')

WORKOUT_ENDPOINT = 'https://app.100daysofpython.dev'


today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")
print(now_time)
print(today_date)

POST_ENDPOINT = f"{WORKOUT_ENDPOINT}/v1/nutrition/natural/exercise"


headers = {
    'x-app-id': WORKOUT_APP_ID,
    'x-app-key': WORKOUT_API_KEY,
}

exercise_text = input('What exercises did you do today? ')

params = {
    'query': exercise_text,
    'weight': 50,
    'height_cm': 164,
    'age': 31,
    'gender': "female",
}

response = requests.post(POST_ENDPOINT, headers=headers, json=params)
response.raise_for_status()

result = response.json()
exercise = result['exercises'][0]['name']

duration = result['exercises'][0]['duration_min']
calories = result['exercises'][0]['nf_calories']

sheety_header = {
    'Authorization': f'Bearer {SHEETY_TOKEN}'
}

data = {
    'workout': {
        'date': today_date,
        'time': now_time,
        'exercise': exercise.title(),
        'duration': duration,
        'calories': calories,
    }
}

print(data)

sheety_post = requests.post(SHEETY_POST_ENDPOINT, json=data, headers=sheety_header)
sheety_post.raise_for_status()
print(sheety_post.text)