import requests
from bs4 import BeautifulSoup


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

