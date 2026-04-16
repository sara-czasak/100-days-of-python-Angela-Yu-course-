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
                episode_airing_index = r.json()['episodes'].index(episode)
                airing = episode['show_id']
                self.notifier.send_notification(airing)
                new_data = self.get_new_date(episode_airing_index, show_id, season_number)
                return airing, new_data
        return None, None


    def get_new_date(self, episode_airing_index, show_id, season_number):
        r = requests.get(f'{self.endpoint}/{show_id}/season/{season_number}', headers={'Authorization': f'Bearer {self.token}'})
        next_episode = r.json()['episodes'][episode_airing_index +1]
        return next_episode


