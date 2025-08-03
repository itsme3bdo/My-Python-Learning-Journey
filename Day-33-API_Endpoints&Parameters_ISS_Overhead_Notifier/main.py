import time

import requests
from future.backports.datetime import datetime
import smtplib
import threading

MY_LAT = your_LAT
MY_LNG = your_LNG


def check():
    response=requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()  #tells us what's wrong if not connected/
                                 # don't get 200
    data =  response.json()

    longitude  =  float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    iss_position =(longitude,latitude)
    print(iss_position)

    if MY_LNG - 5 <= longitude <= MY_LNG + 5 and MY_LAT - 5 <= latitude <= MY_LAT + 5:
        return True,iss_position

# def run_func():
#     thread = threading.Timer(60,run_func)
#     thread.start()
#     check()
#     is_night()
#
# #Your position is within +5 or -5 degrees of the ISS position.

def is_night():

    parameters  = {
        "lat":MY_LAT,
        "lng":MY_LNG,
        "formatted":0
    }
    response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise  = int(data["results"]["sunrise"].split("T")[1].split(":")[0])+3
    sunset  = int(data["results"]["sunset"].split("T")[1].split(":")[0])+3
    now = datetime.now()
    if now.hour>=sunset or now.hour <=sunrise:
        return True

while True:
    print(check())
    time.sleep(60)
    #If the ISS is close to my current position
    if check==True and is_night==True:

        password = "your_smtp_password"
        my_email = "your_email"

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="abdutries@gmail.com",
                                msg=f"Subject:ISS is above you!!!!\n\nLook up!")
        # and it is currently dark
        # Then send me an email to tell me to look up.

