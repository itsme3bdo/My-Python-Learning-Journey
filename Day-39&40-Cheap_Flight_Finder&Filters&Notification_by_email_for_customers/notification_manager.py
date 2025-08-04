import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()

account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")


# This class is responsible for sending notifications with the deal flight details.

class NotificationManager:
    def __init__(self):
        self.number_from = "+12293039281"
        self.number_to =  "your_number"
        self.my_email= os.getenv("my_email")
        self.password = os.getenv("password")
    pass

    def send_text(self,json):
        for x in json:
            price=x["grandPrice"]
            dep = x["departureIATA"]
            arr=x["arrivalIATA"]
            datee = x["departureTime"]
            last = x["lastTicketingDate"]
            client = Client(account_sid, auth_token)
            message = client.messages.create(
            body=f"Price Alert!!!\n\n Low price alert! Only {price}$ to fly from {dep} to {arr}, on"
                 f" {datee} until {last}",
            from_=f"{self.number_from}",
            to=f"{self.number_to}",
            )
            print(message.status)

    def send_email(self,users,json):
        for x in users:
            name = x["whatIsYouFirstName?"]
            lastname = x["whatIsYouLastName?"]
            emaill = x["whatIsYourEmailAddress?"]
            for x in json:
                last = x["lastTicketingDate"]
                price = x["grandPrice"]
                dep = x["departureIATA"]
                arr = x["arrivalIATA"]
                datee = x["departureTime"]
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=self.my_email, password=self.password)
                    connection.sendmail(from_addr=self.my_email,
                                    to_addrs=f"{emaill}",
                                    msg=f"Subject:Low Price Alert!!!\n\nHey {name} {lastname} Low price alert! Only {price}$ to fly from {dep} to {arr}, on"
                                    f" {datee} until {last}")
