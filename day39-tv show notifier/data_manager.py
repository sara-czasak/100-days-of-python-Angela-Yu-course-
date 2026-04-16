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
        self.put_endpoint = os.getenv('SHEETY_PUT_ENDPOINT')


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
                # self.update_data(show_id, show['show'])
                return show['show'], show['id']


    def update_data(self, new_data, today):
        tmbdShowId = new_data['show_id']
        new_episode = new_data['episode_number']
        new_date = new_data['air_date']
        show, row_id = self.find_episode_by_id(tmbdShowId)
        data_to_put = {
            'sheet1': {
                'latestEpisode': new_episode,
                'nextEpisodeDate': new_date,
                'lastEpisodeDate': today,
                'notified': 'yes',
            }
        }
        endpoint = f'{self.put_endpoint}{row_id}'
        r = requests.put(endpoint, headers=self.header, json=data_to_put)
        print(new_data)


if __name__ == '__main__':
    manager = DataManager()
    print(manager.get_show_id_and_season())
