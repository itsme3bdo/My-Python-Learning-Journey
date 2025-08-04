import requests
from datetime import datetime
import os
from dotenv import load_dotenv


load_dotenv()
WEIGHT_KG = 89
HEIGHT_CM = 179
AGE = 24

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
TOKEN = os.getenv("TOKEN")

end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety = "https://api.sheety.co/7b35f3b23800435f9ab966231629ccdd/myWorkouts/workouts"

query=input("Tell me which exercises you did:")

header = {
    "x-app-id":APP_ID,
    "x-app-key":API_KEY}

config={"query":query,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE
        }

response = requests.post(url=end_point, headers=header,json=config)
result = response.json()
header2 = {
    "Authorization":TOKEN
}


for exercise in result["exercises"]:
    date = datetime.now().date()
    time = datetime.now().time()
    con = {"workout":
               {"date":date.strftime("%d/%m/%Y"),
           "time":time.strftime("%X"),
           "exercise":exercise["name"].title(),
           "duration":exercise["duration_min"],
           "calories":exercise["nf_calories"]}}
    response_sheet  = requests.post(url=sheety,headers=header2,json=con)
    print(response_sheet.json())
