import requests

def get_data():

    response = requests.get('https://opentdb.com/api.php?amount=20&category=18&difficulty=medium&type=boolean')
    response.raise_for_status()
    quiz_data = response.json()['results']
    return quiz_data
