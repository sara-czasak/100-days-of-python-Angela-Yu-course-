import datetime
import smtplib
from func import *
import os
from dotenv import load_dotenv


load_dotenv()


# CONSTANTS
my_email = os.getenv('my_email')
app_password = os.getenv('app_password')
to_email = 'sara.p.czasak.m@gmail.com'


now = datetime.datetime.now()
weekday = now.weekday()

# if weekday == 0:
#     with smtplib.SMTP('smtp.gmail.com', 587) as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=app_password)
#         connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=f'Subject: Monday Motivation!\n\n{get_quote()}')

if weekday in [0,1,2,3,4]:
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=f'Subject: Daily Motivation!\n\n{get_quote()}')