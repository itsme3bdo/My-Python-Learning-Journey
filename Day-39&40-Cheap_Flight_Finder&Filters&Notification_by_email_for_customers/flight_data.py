import os
from dotenv import load_dotenv
import requests
from datetime import datetime, timedelta

load_dotenv()

APP_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")


current_date = datetime.now().strftime("%Y-%m-%d")
six_months_from_now = (datetime.now() + timedelta(days=180)).strftime("%Y-%m-%d")
results=[]
aggregated_results = {"responses": []}

def get_access_token():
    endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": APP_KEY,
        "client_secret": API_SECRET
    }
    response = requests.post(url=endpoint, headers=headers, data=data)
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        print(f"Failed to get access token: {response.status_code}")
        print(response.json())
        return None

TOKEN = get_access_token()

headers1 = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.url= "https://test.api.amadeus.com/v2/shopping/flight-offers"
        self.response = ""
        self.data={}
    pass

    def getinfo(self,json):
        for x in json["prices"]:
            self.data={}
            code=x["iataCode"]
            price = x["lowestPrice"]
            self.data = {
                "currencyCode": "USD",
                "originDestinations": [
                    {
                        "id": "1",
                        "originLocationCode": "IST",
                        "destinationLocationCode": f"{code}",
                        "departureDateTimeRange": {
                            "date": "2025-01-20"
                        },
                    }
                ],
                "travelers": [
                    {"id": "1", "travelerType": "ADULT"}
                ],
                "sources": ["GDS"],
                "searchCriteria": {
                    "maxFlightOffers": 100,
                    "maxPrice": int(price),
                }
            }
            response = requests.post(url=self.url,json=self.data,headers=headers1)
            # print(self.response.json())
            # results.append(response.json())
            aggregated_results["responses"].append(response.json())
            print("\n#############################")
        return aggregated_results