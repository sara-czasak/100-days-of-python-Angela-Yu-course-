import requests
from bs4 import BeautifulSoup
import os
import dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth


dotenv.load_dotenv()

# CONSTANTS
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
SPOTIFY_USERNAME = os.getenv('SPOTIFY_USERNAME')


date = input('Which year do you want to travel to? (YYYY-MM-DD): ')


header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'
    }


ENDPOINT = f'https://web.archive.org/web/20190721180024/https://www.billboard.com/charts/hot-100/{date}'


r = requests.get(url=ENDPOINT, headers=header)

soup = BeautifulSoup(r.content, 'html.parser')

# Getting all song titles
titles = soup.find_all(name='span', class_='chart-list-item__title-text')
titles = [i.text.strip() for i in titles]


scope = 'playlist-modify-private'

REDIRECT_URI = 'https://example.com'

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        cache_path='token.txt'
    )
)

user_id = sp.current_user()['id']
print(user_id)