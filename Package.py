
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

        self.status = "At the Hub"
        self.departure_time = None
        self.delivery_time = None
        
    #print the details of each package
    def __str__(self) -> str:
        return f"Package {self.package_id}: {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.delivery_deadline}, {self.weight}, {self.special_notes}"
    
