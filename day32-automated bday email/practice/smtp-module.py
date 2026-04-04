import datetime
import smtplib


# CONSTANTS
my_email = 'rainbowsperler@gmail.com'
app_password = 'yrki auau xfot ftqt'
to_email = 'sara.p.czasak.m@gmail.com'

today = datetime.date.today()

# connection = smtplib.SMTP('smtp.gmail.com', port=587)
# # Make connection secure
# connection.starttls()
# connection.login(user=my_email, password=app_password)
#
# connection.sendmail(from_addr=my_email, to_addrs='sara.p.czasak.m@gmail.com', msg=f'Subject:This is the subject\n\nThis is the email body.')
# connection.close()

# Better version that closes smtp connection automatically
with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
    # Make connection secure
    connection.starttls()
    connection.login(user=my_email, password=app_password)

    connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=f'Subject:This is the subject\n\nThis is the email body.')