import requests
from twilio.rest import Client

OMW_Endpoint = "https://api.openweathermap.org"

account_sid = "AC31692a5c75db15273581b90911bdd33a"
auth_token = "a4eb58394a59de1f054f955f8fc957d1"
api_key = "b28afb772f06b1bccd195d0220262e64"

weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
    "exclude": "current, minutely, daily"
}

response = requests.get(OMW_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an Umbrella!",
        from_="+14055927351",
        to="2349079658430"
    )

    print(message.sid)
