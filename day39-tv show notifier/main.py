import datetime as dt
from check_latest import *


dotenv.load_dotenv()


# Constants
today = dt.date.today().strftime('%Y-%m-%d')
# today = '2026-04-30'

data_manager = DataManager()
data = data_manager.get_data()
latest_season = str(data[0]['latestSeason'])
show_id = str(data[0]['tmbdShowId'])
new_episode_date = data[0]['nextEpisodeDate']


check_latest = CheckLatest()

show_data = data_manager.get_show_id_and_season()

for show in show_data:
    episode, new_data = check_latest.find_newest_episode(show[0], show[1], today)
    if episode is not None and new_data is not None:
        data_manager.update_data(new_data, today)

