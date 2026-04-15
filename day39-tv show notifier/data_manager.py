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


    def get_show_id_and_season(self):
        data = self.get_data()
        data_list = []
        for i in data:
            data_list.append((i['tmbdShowId'], i['latestSeason']))
        return data_list


    def find_episode_by_id(self, show_id):
        data = self.get_data()
        for show in data:
            if show['tmbdShowId'] == show_id:
                self.update_data(show_id, show['show'])
                return show['show']


    def update_data(self, show_id, show_name):
        data = self.get_data()
        for show in data:
            if show['tmbdShowId'] == show_id:
                current_latest = show['latestEpisode']
                new_latest = int(current_latest) + 1
                json = {
                    'show': show_name,
                    'tmbdShowId': show_id,
                    'latestEpisode': new_latest,
                }
                r = requests.post(self.post_endpoint, headers=self.header, json={})


if __name__ == '__main__':
    manager = DataManager()
    print(manager.get_show_id_and_season())
