# https://openweathermap.org/api/geocoding-api
# https://www.youtube.com/watch?v=bKCORrHbutQ

import requests
from datetime import datetime

kelvin = 273.15

print("Current Weather\nFrom which city do you want to know the weather?")
city = input()
print("\nCurrently Loading......\n")
response_location = requests.get(
    "http://api.openweathermap.org/geo/1.0/direct?q=" + city + "&limit=1&appid={apiKey}") #apikey needs to be filled in
# print(response_location.status_code) # 200 means succesfull connection
# print(response_location.json())
if response_location.status_code == 200:
    print("Getting Location successful\n")
else:
    print("Getting Location unsuccessful\n")
latitude = response_location.json()[0]['lat']
longitude = response_location.json()[0]['lon']
# print(latitude)
# print(longitude)

response_weather = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=" + str(latitude) + "&lon=" + str(
    longitude) + "&appid={apiKey") # apiKey needs to be filled in
# print(response_weather.status_code)
# print(response_weather.json())
if response_weather.status_code == 200:
    print("Getting Weather successful\n")
else:
    print("Getting Weather unsuccessful\n")

print("Weather: " + response_weather.json()['weather'][0]['main'])
print("Description: " + response_weather.json()['weather'][0]['description'])
print("Temperature: " + str(round(response_weather.json()['main']['temp'] - kelvin, 2)) + "°C")
print("Temperature feels like: " + str(round(response_weather.json()['main']['feels_like'] - kelvin, 2)) + "°C")
print("Humidity: " + str(response_weather.json()['main']['humidity']) + "%")

print("Timezone(From UTC Time: " + str(int(response_weather.json()['timezone'] / 3600)) + ")")
print("Current time: " + str(datetime.now().strftime('%H:%M:%S')))
print("Current Date: " + str(datetime.now().date()))
