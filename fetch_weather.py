
import requests
import json

api_key = "your_api_key_here"
city = "London"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    weather_data = response.json()
    print(json.dumps(weather_data, indent=4))
else:
    print("Failed to retrieve data:", response.status_code)
