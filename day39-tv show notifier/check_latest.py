import requests
import os
import dotenv


dotenv.load_dotenv()


class CheckLatest:
    def __init__(self):
        self.endpoint = os.getenv('TMBD_SHOW_DETAILS_ENDPOINT')
        self.token = os.getenv('TMBD_READ_ACCESS_TOKEN')
        self.api = os.getenv('TMDB_API')


    def find_newest_episode(self, show_data, today):
        for i in show_data:
            r = requests.get(f'{self.endpoint}/{i[0]}/season/{i[1]}', headers={'Authorization': f'Bearer {self.token}'})
            for episode in r.json()['episodes']:
                if episode['air_date'] == today:
                    return episode['show_id']
        return 'no episode today'



