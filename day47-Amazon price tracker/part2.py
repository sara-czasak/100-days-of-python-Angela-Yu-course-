import requests
from bs4 import BeautifulSoup
import smtplib
import os
import dotenv

dotenv.load_dotenv()


# CONSTANTS
ENDPOINT = 'https://www.amazon.com/Instant-Vortex-Plus-Air-Fryer/dp/B07VHFMZHJ/ref=sr_1_1_sspa?crid=1076T0HUGFY87&dib=eyJ2IjoiMSJ9.-mbv06IKWwwXSYbPZ3NBroNTg4zaUK6oRPFiwby-DJ3WMkX0tbkB0M_hJxVynWpVHlb3PdZJwEEJFvrdL65ABeHJ41Bwz442fk38-UFhdP2cpup0f4WY5Oq29bHjCK3KeH5IatAx3VfbxxpRna-TCciBRbVw0oLuAuJjc2Nedlmb8jSwJr8_NHXiGu2wyE1yKQuIgakG4n-UEC_uOmk63o8Giu4hLD-g1dYp0u-6VwU.FuXrTrzfk4rsPwXC-MBnkuT2Pivh_IQlkfw9HSxzG6o&dib_tag=se&keywords=instant%2Bpot&qid=1776600174&sprefix=instant%2Bpo%2Caps%2C242&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1'
headers = {
    'User-Agent': 'CCBot/2.0 (https://commoncrawl.org/faq/)',
    'Accept-Language': 'en-US,en;q=0.5',
}
TARGET_PRICE = 100.00
MY_EMAIL = os.getenv('my_email')
APP_PASSWORD = os.getenv('app_password')

# Make a request and soup
soup_ingredients = requests.get(ENDPOINT, headers=headers).content

soup = BeautifulSoup(soup_ingredients, 'html.parser')

whole_price = soup.find(name='span', class_='a-price-whole').text


price_decimal = soup.find(name='span', class_='a-price-fraction').text

price = float(whole_price + price_decimal)

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