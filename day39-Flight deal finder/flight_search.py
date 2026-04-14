import os
import dotenv
import requests


dotenv.load_dotenv()


GOOGLE_FLIGHTS_ENDPOINT = 'https://serpapi.com/search?engine=google_flights'



class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key = os.getenv("SERPY_API")


    def search_flight(self, arrival_id, outbound_date, return_date):
        params = {
            "engine": "google_flights",
            "departure_id": 'KRK',
            "arrival_id": arrival_id,
            "outbound_date": outbound_date,
            "return_date": return_date,
            "type": "1",
            "adults": "1",
            "currency": "PLN",
            "api_key": self.api_key,
        }
        r = requests.get(GOOGLE_FLIGHTS_ENDPOINT, params=params)
        if r.status_code != 200:
            print(f"search_flights() response code: {r.status_code}")
            return None
        data = r.json()
        if "error" in data:
            print(f"API error: {data['error']}")
            return None
        return r.json()