# WGU C950 Project
# Student ID: 012276101
# Christopher Alagna

from csv_reader import load_package_data, load_distance_data
from hash_table import HashTable
from distances import get_distance
from datetime import datetime, timedelta
from truck import Truck
from delivery import deliver_packages

#initialize hash table and load package data from CSV
hash_table = HashTable()
load_package_data("WGUPS_Packages.csv", hash_table)

#load distance data, create address map and distance matrix
address_map, distance_matrix = load_distance_data("WGUPS_Distances.csv")

#first truck departures are staggered due to delay in flight arrival for packages 6, 25, 28, 32.
start_time_truck_1 = timedelta(hours=8)
start_time_truck_2 = timedelta(hours=9, minutes=5)

#instantiate 3 truck objects
truck_1 = Truck(1)
truck_2 = Truck(2)
truck_3 = Truck(3)

#load the first 2 trucks with packages
truck_1.load(hash_table, start_time_truck_1)
truck_2.load(hash_table, start_time_truck_2)

#two drivers leave hub at 8am to deliver packages
return_time_1 = deliver_packages(truck_1, address_map, distance_matrix, start_time_truck_1)
return_time_2 = deliver_packages(truck_2, address_map, distance_matrix, start_time_truck_2)

#whichever truck gets back first loads truck 3 with the remaining packages to be delivered
if return_time_1 < return_time_2:
    truck_3.load(hash_table, return_time_1)
    return_time_3 = deliver_packages(truck_3, address_map, distance_matrix, return_time_1)
else:
    truck_3.load(hash_table, return_time_2)
    return_time_3 = deliver_packages(truck_3, address_map, distance_matrix, return_time_2)

#calculate total truck mileage for display in UI
total_mileage = truck_1.mileage + truck_2.mileage + truck_3.mileage
#start of user interaction. User enter a time and program outputs all package statuses at that time
print("=" * 50)
print("WESTERN GOVERNORS UNIVERSITY PARCEL SERVICE")
print(f"Total Route Mileage: {total_mileage:.2f} miles")
print(f"Truck 1: {truck_1.mileage:.2f} miles | Truck 2: {truck_2.mileage:.2f} miles | Truck 3: {truck_3.mileage:.2f} miles")
print("=" * 50)

while True:
    print("\nSelect an option:")
    print("1. View status of ALL packages at a specific time")
    print("2. Look up a SINGLE package at a specific time")
    print("3. View total truck mileage")
    print("4. Exit")
    
    choice = input("Enter choice (1-4): ").strip()

    if choice in ("1", "2"):
        user_time = input("Enter a time (HH:MM e.g. 09:00): ").strip()
        try:
            #convert user time to datetime object
            parts = [int(x) for x in user_time.split(":")]
            if len(parts) != 2 or not (0 <= parts[0] <= 23) or not (0 <= parts[1] <= 59):
                print("Invalid time format. Please use HH:MM.")
                continue
            user_time = timedelta(hours=parts[0], minutes=parts[1])
        except ValueError:
            print("Invalid time format. Please use HH:MM.")
            continue

        if choice == "1":
            print(f"\nAll package statuses at {user_time}")
            for i in range(1, 41):
                package = hash_table.search_package(i)
                if package:
                    print(package.get_status_at_time(user_time))
        else:
            try:
                print(f"\nPackage status at {user_time}")
                package_id = int(input("Enter package ID: ").strip())
                package = hash_table.search_package(package_id)
                if package:
                    print(f"Package {package_id} Status at {user_time}")
                    print(package.get_status_at_time(user_time))
                else:
                    print(f"Package {package_id} not found.")
            except ValueError:
                print("Invalid package ID.")

    elif choice == "3":
        print(f"\nTruck 1: {truck_1.mileage:.2f} miles")
        print(f"Truck 2: {truck_2.mileage:.2f} miles")
        print(f"Truck 3: {truck_3.mileage:.2f} miles")
        print(f"Total mileage: {total_mileage:.2f} miles")
        
    elif choice == "4":
        print("\nExiting application...")
        break
    else:
        print("Invalid choice. Please try again.")

