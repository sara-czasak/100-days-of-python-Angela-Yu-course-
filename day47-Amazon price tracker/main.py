import requests
from bs4 import BeautifulSoup


AMAZON_CLONE_ENDPOINT = 'https://appbrewery.github.io/instant_pot/'

r = requests.get(AMAZON_CLONE_ENDPOINT)

soup = BeautifulSoup(r.content, 'html.parser')
price_whole = soup.find(name='span', class_='a-price-whole').text

price_decimal = soup.find(name='span', class_='a-price-fraction').text

price = float(price_whole + price_decimal)

