import requests
from datetime import datetime


APP_KEY = "516edc69975114e938d4683a7e281db2"
APP_ID = "76c8eb29"
GENDER = "female"
WEIGHT = 54
HEIGHT = 153
AGE = 18

tracker_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": APP_ID,
    "x-app-key":APP_KEY
}

parameters = {
 "query": input("Tell me what exercise you did: "),
 "gender":GENDER,
 "weight_kg":WEIGHT,
 "height_cm":HEIGHT,
 "age":AGE
}
today =  datetime.now()


response = requests.post(url=tracker_endpoint,headers=headers,json=parameters)
data = response.json()


for exercise_data in data["exercises"]:
    update_parameters = {
        "sheet1": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": exercise_data['name'].title(),
            "duration":exercise_data['duration_min'],
            "calories": exercise_data['nf_calories']

        }
    }

response1 = requests.post(url="https://api.sheety.co/bfac72cf8a8f2a4e9b2a243d7253679e/myWorkouts/sheet1",json=update_parameters,auth=(
      "Soundarya",
      "So1234567",
  ))