import requests
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint


data_manager = DataManager()

print(data_manager.get_destinations_data())


