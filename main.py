import requests
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint


data_manager = DataManager()
data = data_manager.get_destinations_data()

flight_search = FlightSearch()
for row in data:
    row["iataCode"] = flight_search.get_codes(row['city'])

data_manager.destination_data = data
data_manager.update_sheet()





