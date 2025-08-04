import requests
import os
from dotenv import load_dotenv

load_dotenv()
response = ""
alll=[]
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.url_prices = os.getenv("url_prices")
        self.url_users = os.getenv("url_users")
        self.header = {"Authorization": "Bearer damnsoncomeforme"}
        self.response = ""
        self.customers={}
    pass

    def getit(self):
        self.response = requests.get(url=self.url_prices,headers=self.header)
        return self.response.json()
    def get_customer_emails(self):
        response = requests.get(url=self.url_users,headers=self.header)
        ans = response.json()["users"]
        return ans


