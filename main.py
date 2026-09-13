from csv_reader import load_package_data, load_distance_data
from hash_table import HashTable
from distances import get_distance
from datetime import datetime, timedelta
from truck import Truck
from delivery import deliver_packages

#initialize hash table and load package data from CSV
hash_table = HashTable()
load_package_data("WGUPS_Packages.csv", hash_table)

#search for and print all packages
#for i in range(1, 41):
#    package = hash_table.search_package(i)
#    print(package)

#load distance data, create address map and distance matrix
address_map, distance_matrix = load_distance_data("WGUPS_Distances.csv")

#print distance matrix for verification
#for i in range(len(distance_matrix)):
#    print(distance_matrix[i])

#print distance between two addresses
#distance = get_distance("1060 Dalton Ave S", "195 W Oakland Ave", address_map, distance_matrix)
#print(f"Distance between 1060 Dalton Ave S and 195 W Oakland Ave: {distance} miles")

#start at 8am
start_time = timedelta(hours=8)

#instantiate 3 truck objects
truck_1 = Truck(1)
truck_2 = Truck(2)
truck_3 = Truck(3)

#loading trucks with packages
truck_1.load(hash_table)
truck_2.load(hash_table)
truck_3.load(hash_table)

#print all packages with delivery times
#for i in range(1, 41):
#    package = hash_table.search_package(i)
#    print(package)

#two drivers leave hub at 8am to deliver packages
return_time_1 = deliver_packages(truck_1, address_map, distance_matrix, start_time)
return_time_2 = deliver_packages(truck_2, address_map, distance_matrix, start_time)

#whoever gets back first delivers the remaining packages
if return_time_1 < return_time_2:
    truck_3_departure_time = return_time_1
    print(f"\n\nTruck 1 has returned at {return_time_1} and will now operate Truck 3 to take out remaining packages.")
    print(f"Truck 2 has returned at {return_time_2}.")
    return_time_3 = deliver_packages(truck_3, address_map, distance_matrix, truck_3_departure_time)
    print(f"\n\nTruck 3 has returned at {return_time_3} and has delivered all remaining packages.")
else:
    truck_3_departure_time = return_time_2
    print(f"\n\nTruck 2 has returned at {return_time_2} and will now operate Truck 3 to take out remaining packages.")
    print(f"Truck 1 has returned at {return_time_1}.")
    return_time_3 = deliver_packages(truck_3, address_map, distance_matrix, truck_3_departure_time)
    print(f"\n\nTruck 3 has returned at {return_time_3} and has delivered all remaining packages.")