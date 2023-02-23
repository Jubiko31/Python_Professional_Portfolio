import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from random import choice
from dotenv import load_dotenv
load_dotenv()

ONE_API = "https://the-one-api.dev/v2"
API_KEY = os.getenv('API_KEY')
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
tw_number = os.getenv('TWILIO_TRIAL_NUMBER')
tel = os.getenv('TEL')

one_api_headers = {
    "Authorization": API_KEY
}

res = requests.get(f"{ONE_API}/quote", headers=one_api_headers)
res.raise_for_status()

data = res.json()["docs"]

day_quote = choice(data)
movie_id = day_quote["movie"]
char_id = day_quote["character"]

quote = day_quote["dialog"]
movie = requests.get(f"{ONE_API}/movie/{movie_id}", headers=one_api_headers).json()["docs"][0]["name"]
character = requests.get(f"{ONE_API}/character/{char_id}", headers=one_api_headers).json()["docs"][0]["name"]

print(f"{quote} \n--{character} | {movie}")

if day_quote:
    proxy_client = TwilioHttpClient()
    client = Client(account_sid, auth_token, http_client=proxy_client)
    msg = client.messages \
        .create(
            body=f"\n\n{quote} \n--{character} | {movie}",
            from_=tw_number, 
            to=tel 
        )
    print(msg.status)