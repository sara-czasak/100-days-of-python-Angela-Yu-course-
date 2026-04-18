import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


# !!! Use .content not .text, .text sometimes decodes the html badly leaving some html encoding in !!!
r = requests.get(URL).content
soup = BeautifulSoup(r, 'html.parser')

titles = soup.find_all(name='h3', class_='title')
with open('movies.txt', 'w', encoding='UTF-8') as f:
    for title in titles[::-1]:
        f.write(f'{title.text}\n')
