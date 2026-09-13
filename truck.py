from hash_table import HashTable

class Truck:
    
    def __init__(self, truck_number):
        self.truck_number = truck_number
        self.packages = []
        self.mileage = 0.0
        self.current_location = "HUB"
        self.speed = 18.0
    
    #loads up to 16 packages onto the truck
    def load(self, hash_table: HashTable):
        if self.truck_number == 1:
            for i in range(1, 16):
                package = hash_table.search_package(i)
                self.packages.append(package)
        elif self.truck_number == 2:
            for i in range(16, 32):
                package = hash_table.search_package(i)
                self.packages.append(package)
        elif self.truck_number == 3:
            for i in range(32, 41):
                package = hash_table.search_package(i)
                self.packages.append(package)

    
            

            
    
    