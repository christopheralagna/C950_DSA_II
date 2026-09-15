from hash_table import HashTable
from datetime import datetime

class Truck:
    
    def __init__(self, truck_number):
        self.truck_number = truck_number
        self.packages = []
        self.mileage = 0.0
        self.current_location = "HUB"
        self.speed = 18.0
        self.departure_time = None

    #PACKAGE REQUIREMENTS--------------------------------------------------------------------------
    #packages 3, 18, 36, 38 must be on truck 2
    #packages 6, 25, 28, 32 are on truck 2 due to delay of flight arrival.
    #package 14 is delivered with 15 and 19.
    #package 16 is delivered with 13 and 19.
    #package 20 is delivered with 13 and 15.
    #10:30am deadline: 1, 6, 13, 14, 16, 20, 25, 29, 30, 31, 34, 37, 40. Put on truck 1 or 2 to ensure deadline is met.
    #9:00am deadline: 15. Put on truck 1 to ensure deadline is met.
    #package 9 is put on truck 3 to delay it until 10:20 am (incorrect address)
    #----------------------------------------------------------------------------------------------

    truck_1_packages = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40, 7]
    truck_2_packages = [3, 6, 18, 25, 26, 28, 32, 36, 38, 17, 21, 22, 24, 33]
    truck_3_packages = [2, 4, 5, 8, 9, 10, 11, 12, 23, 27, 35, 39]
    
    #loads packages onto truck based on package list
    def load(self, hash_table: HashTable, departure_time: datetime):
        if self.truck_number == 1:
            for i in self.truck_1_packages:
                package = hash_table.search_package(i)
                package.departure_time = departure_time
                package.truck_number = 1
                self.packages.append(package)
        elif self.truck_number == 2:
            for i in self.truck_2_packages:
                package = hash_table.search_package(i)
                package.departure_time = departure_time
                package.truck_number = 2
                self.packages.append(package)
        elif self.truck_number == 3:
            for i in self.truck_3_packages:
                package = hash_table.search_package(i)
                package.departure_time = departure_time
                package.truck_number = 3
                self.packages.append(package)

    
            

            
    
    