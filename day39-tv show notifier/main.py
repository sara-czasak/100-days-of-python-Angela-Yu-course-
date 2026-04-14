import requests
import dotenv
import os
from pprint import pprint
import datetime as dt
from data_manager import *
from check_latest import *


dotenv.load_dotenv()


# Constants
# today = dt.date.today().strftime('%Y-%m-%d')
today = '2026-04-30'

data_manager = DataManager()
data = data_manager.get_data()
latest_season = str(data[0]['latestSeason'])
show_id = str(data[0]['tmbdShowId'])
new_episode_date = data[0]['nextEpisodeDate']

check_latest = CheckLatest()


episodes = check_latest.find_newest_episode(data_manager.get_show_id_and_season(), today)
pprint(episodes)
