#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from datetime import datetime,timedelta
import os
from dotenv import load_dotenv
from notification_manager import NotificationManager
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch

load_dotenv()

dataa = DataManager()
ans = dataa.getit()
users = dataa.get_customer_emails()

# print(ans)
# ans = {'prices': [{'city': 'Paris', 'iataCode': 'CDG', 'lowestPrice': 90, 'id': 2}, {'city': 'Frankfurt', 'iataCode': 'FRA', 'lowestPrice': 90, 'id': 3}, {'city': 'Tokyo', 'iataCode': 'NRT', 'lowestPrice': 364, 'id': 4}, {'city': 'Hong Kong', 'iataCode': 'HKG', 'lowestPrice': 413, 'id': 5}, {'city': 'Moscow', 'iataCode': 'SVO', 'lowestPrice': 98, 'id': 6}, {'city': 'Amsterdam', 'iataCode': 'AMS', 'lowestPrice': 95, 'id': 7}, {'city': 'Dubai', 'iataCode': 'DXB', 'lowestPrice': 202, 'id': 8}, {'city': 'London', 'iataCode': 'LHR', 'lowestPrice': 100, 'id': 9}, {'city': 'Rome', 'iataCode': 'FCO', 'lowestPrice': 47, 'id': 10}]}
flightdata = FlightData()
info2 =  flightdata.getinfo(ans)


flight_search = FlightSearch()
end = flight_search.getinfo(info2["responses"][0])

tell_me = NotificationManager()
# tell_me.send_text(end)
tell_me.send_email(users,end)

# print(info2)
# print(type(info2))
print(end)





