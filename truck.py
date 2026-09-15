from hash_table import HashTable

class Truck:
    
    def __init__(self, truck_number):
        self.truck_number = truck_number
        self.packages = []
        self.mileage = 0.0
        self.current_location = "HUB"
        self.speed = 18.0

    #package lists for each truck. Ensured that all special instructions are factored into delivery.
    #packages 3, 18, 36, 38 must be on truck 2
    #packages 6, 25, 28, 32 are on truck 3 due to delay of flight arrival
    #package 14 is delivered with 15 and 19.
    #package 16 is delivered with 13 and 19.
    #package 20 is delivered with 13 and 15.
    #package 9 is put on truck 3 to delay it until 10:20 am (incorrect address)
    truck_1_packages = [1, 2, 4, 5, 7, 8, 10, 11, 12, 13, 14, 15, 16, 19, 20, 35]
    truck_2_packages = [3, 17, 18, 21, 22, 23, 24, 26, 27, 29, 30, 31, 33, 34, 36, 38]
    truck_3_packages = [6, 9, 25, 28, 32, 37, 39, 40]
    
    #loads packages onto truck based on package list
    def load(self, hash_table: HashTable):
        if self.truck_number == 1:
            for i in self.truck_1_packages:
                package = hash_table.search_package(i)
                self.packages.append(package)
        elif self.truck_number == 2:
            for i in self.truck_2_packages:
                package = hash_table.search_package(i)
                self.packages.append(package)
        elif self.truck_number == 3:
            for i in self.truck_3_packages:
                package = hash_table.search_package(i)
                self.packages.append(package)

    
            

            
    
    