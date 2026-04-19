import requests
from bs4 import BeautifulSoup
import smtplib
import os
import dotenv


dotenv.load_dotenv()

# CONSTANTS
AMAZON_CLONE_ENDPOINT = 'https://appbrewery.github.io/instant_pot/'
TARGET_PRICE = 100.00
MY_EMAIL = os.getenv('my_email')
APP_PASSWORD = os.getenv('app_password')

# Getting current price of instant pot as a float
r = requests.get(AMAZON_CLONE_ENDPOINT)

soup = BeautifulSoup(r.content, 'html.parser')
price_whole = soup.find(name='span', class_='a-price-whole').text

price_decimal = soup.find(name='span', class_='a-price-fraction').text

price = float(price_whole + price_decimal)

# Send email alert if price is below target price
if price < TARGET_PRICE:
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=APP_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f'Subject: Price Alert\n\nThe price is under your target price! Current instant pot price: {price}$'
        )