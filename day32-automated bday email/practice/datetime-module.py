import datetime as dt

date = dt.date.today()
year = date.year
month = date.month
day = date.day
day_of_week = date.weekday()


my_dob = dt.datetime(1995, 2, 25, hour=16, minute=40)
print(my_dob)
