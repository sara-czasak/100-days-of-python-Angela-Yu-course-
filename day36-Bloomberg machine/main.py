import requests
import os
import dotenv
from datetime import datetime, timedelta
from twilio.rest import Client


dotenv.load_dotenv()

STOCK_API = os.getenv('STOCK_API')
NEWS_API = os.getenv('NEWS_API')
TWILIO_API = os.getenv('TWILIO_API')
TWILIO_NUMBER = os.getenv('TWILIO_NUMBER')
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


stock_params ={
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': STOCK_API,
}


news_params ={
    'apiKey': NEWS_API,
    'q': COMPANY_NAME,
}


response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()


yesterday = str((datetime.now() - timedelta(1)).date())

yesterday_closing_price = data['Time Series (Daily)'][yesterday]['4. close']

day_before_yesterday = str((datetime.now() - timedelta(2)).date())

day_before_yesterday_closing_price = data['Time Series (Daily)'][day_before_yesterday]['4. close']

differance_real = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
differance_abs = abs(differance_real)

percentage = differance_abs / float(yesterday_closing_price) * 100

if percentage >= 5:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    headline_1 = news_response.json()['articles'][0]['title']
    description_1 = news_response.json()['articles'][0]['description']
    headline_2 = news_response.json()['articles'][1]['title']
    description_2 = news_response.json()['articles'][1]['description']
    headline_3 = news_response.json()['articles'][2]['title']
    description_3 = news_response.json()['articles'][2]['description']
    articles = [(headline_1, description_1), (headline_2, description_2), (headline_3, description_3)]
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    for i in articles:
        if differance_real < 0:
            message = client.messages.create(
                body=f"""{COMPANY_NAME}: 🔻{percentage:.2f}%
                        headline: {i[0]}\n
                        brief: {i[1]}""",
                from_=TWILIO_NUMBER,
                to="+48692948897",
            )
        else:
            message = client.messages.create(
                body=f"""{COMPANY_NAME}: 🔺{percentage:.2f}%
                                   headline: {i[0]}\n
                                   brief: {i[1]}""",
                from_=TWILIO_NUMBER,
                to="+48692948897",
            )
else:
    print("Nothing to report today")