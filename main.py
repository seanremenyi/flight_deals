from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
data = data_manager.get_destinations_data()
flight_search = FlightSearch()
notification_manager = NotificationManager

ORIGIN_CITY_IATA = "MEL"

for row in data:
data_manager.destination_data = data
data_manager.update_sheet()

tomorrow = datetime.now() + timedelta(days=1)
six_months = datetime.now() + timedelta(days=(6 *30))

for destination in data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months
    )
    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to "
                    f"{flight.destination_city}-{flight.destination_airport}, from {flight.out_date} "
                    f"to {flight.return_date}."
        )

