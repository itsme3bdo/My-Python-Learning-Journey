# import smtplib
#
# password  = "your_password"
# my_email  = "your_email"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="abdutries@gmail.com",
#                         msg = "Subject:Hello\n\nThis is the body of my email.")
#
import datetime as dt
import smtplib
from random import choice

now  = dt.datetime.now()
year = now.year
month = now.month
dayoftheweek = now.weekday()

# date_of_birth = dt.datetime(year=2000,month=4,day=2)
with open("quotes.txt","r") as quotes:
    data = quotes.readlines()
    todaysq = choice(data)
    print(todaysq)

if dayoftheweek == 1:
    password  = "your_password"
    my_email  = "your_email"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="abdutries@gmail.com",
                            msg = f"Subject:Good Morning Boss\n\n{todaysq}")
