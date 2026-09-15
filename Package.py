from datetime import datetime, timedelta

class Package:
    
    #initialize package object. Hashable on package_id
    def __init__(self, package_id: int, address: str, city: str, state: str, zip_code: str, delivery_deadline: str, weight: int, special_notes: str) -> None:
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.special_notes = special_notes

        self.departure_time = None
        self.delivery_time = None
        self.truck_number = None

    def get_status_at_time(self, query_time: timedelta) -> str:
        #determine the address for package 9 if current_time is at or after 10:20 am
        if self.package_id == 9:
            if query_time < timedelta(hours=10, minutes=20):
                self.address = "300 State St"
                self.zip_code = "84103"
            else:
                self.address = "410 S State St"
                self.zip_code = "84111"
        
        #package is at hub if query time is before departure time
        if query_time < self.departure_time:
            status = "At Hub"
            #packages that have been delayed are not at hub until 9:05 am
            if self.package_id in [6, 25, 28, 32] and query_time < timedelta(hours=9, minutes=5):
                status = "DELAYED, has not yet reached the Hub"
            return (f"Package {self.package_id} | Status: {status} | Address: {self.address}, {self.city}, {self.state}, {self.zip_code} | Delivery Deadline: {self.delivery_deadline} | Weight: {self.weight} | Special Notes: {self.special_notes}")
        #package is out for delivery if query time is between departure and delivery time
        elif query_time >= self.departure_time and query_time < self.delivery_time:
            status = "Out for Delivery"
            return (f"Package {self.package_id} | Status: {status} | Truck: {self.truck_number} | Departure Time: {self.departure_time} | Address: {self.address}, {self.city}, {self.state}, {self.zip_code} | Delivery Deadline: {self.delivery_deadline} | Weight: {self.weight} | Special Notes: {self.special_notes}")
        #package is delivered if query time is after delivery time
        elif query_time >= self.delivery_time:
            status = "Delivered"
            return (f"Package {self.package_id} | Status: {status} | Truck: {self.truck_number} | Departure Time: {self.departure_time} | Delivery Time: {self.delivery_time} | Address: {self.address}, {self.city}, {self.state}, {self.zip_code} | Delivery Deadline: {self.delivery_deadline} | Weight: {self.weight} | Special Notes: {self.special_notes}")

    #print the details of each package
    def __str__(self) -> str:
        return f"Package {self.package_id}: {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.delivery_deadline}, {self.weight}, {self.special_notes}"
    
