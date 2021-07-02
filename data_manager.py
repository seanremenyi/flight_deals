import requests

sheety_endpoint = ""



class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destinations_data(self):
        response = requests.get(url=sheety_endpoint)
        results = response.json()
        self.destination_data = results["prices"]
        return self.destination_data

