import requests


def get_weather(city):
    url = f"https://api.tomorrow.io/v4/weather/realtime?location={city}&apikey=NX6j4SODwtlAC3FCOLIXc6kwsDZMZU0R"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)

    data = response.json()
    return data["data"]["values"]["temperature"]
