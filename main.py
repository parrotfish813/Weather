import requests
import json

API_KEY = "079388ee5b8401915541c3c044716bd0"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(requests_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temp = round(((data['main']['temp'] - 273.15) * (9 / 5) + 32), 2)
    print("Weather: ", weather)
    print("Temperature: ", temp, "F")

else:
    print("An error occured")
