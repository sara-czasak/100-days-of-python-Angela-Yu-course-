import csv
import smtplib
import datetime as dt
from func import *
import os
from dotenv import load_dotenv


load_dotenv()

# CONSTANTS
my_email = os.getenv('my_email')
app_password = os.getenv('app_password')


year = dt.date.today().year
month = dt.date.today().month
day = dt.date.today().day


with open('bdays.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[3] == str(month) and row[4] == str(day):
            card = write_card(row[0], row[2], year)
            with smtplib.SMTP('smtp.gmail.com', 587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=app_password)
                connection.sendmail(
                    from_addr=my_email, to_addrs='sara.p.czasak.m@gmail.com', msg=f'Subject:Happy Birthday!!!\n\n{card}'
                )

