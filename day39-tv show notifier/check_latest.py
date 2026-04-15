import requests
import os
import dotenv
from notifier import *

dotenv.load_dotenv()


class CheckLatest:
    def __init__(self):
        self.endpoint = os.getenv('TMBD_SHOW_DETAILS_ENDPOINT')
        self.token = os.getenv('TMBD_READ_ACCESS_TOKEN')
        self.api = os.getenv('TMDB_API')
        self.notifier = Notifier()


    def find_newest_episode(self, show_id, season_number, today):
        r = requests.get(f'{self.endpoint}/{show_id}/season/{season_number}', headers={'Authorization': f'Bearer {self.token}'})
        for episode in r.json()['episodes']:
            if episode['air_date'] == today:
                airing = episode['show_id']
                self.notifier.send_notification(airing)
                return airing
        return "No episode today"



