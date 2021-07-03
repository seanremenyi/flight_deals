import requests

KIWI_API_ENDPOINT = "https://tequila-api.kiwi.com"
KIWI_API_KEY = ""


class FlightSearch:

    def get_codes(self, city):
        endpoint = f"{KIWI_API_ENDPOINT}/locations/query"
        headers = {"apikey": KIWI_API_KEY}
        query = {"term": city, "location_types": "city"}
        response = requests.get(url=endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code