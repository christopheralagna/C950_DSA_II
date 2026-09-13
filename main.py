from csv_reader import load_package_data, load_distance_data
from hash_table import HashTable
from distances import get_distance

#initialize hash table and load package data from CSV
hash_table = HashTable()
load_package_data("WGUPS_Packages.csv", hash_table)

#search for and print all packages
for i in range(1, 41):
    package = hash_table.search_package(i)
    print(package)

#load distance data, create address map and distance matrix
address_map, distance_matrix = load_distance_data("WGUPS_Distances.csv")

#print distance matrix for verification
for i in range(len(distance_matrix)):
    print(distance_matrix[i])

distance = get_distance("1060 Dalton Ave S", "195 W Oakland Ave", address_map, distance_matrix)
print(f"Distance between 1060 Dalton Ave S and 195 W Oakland Ave: {distance} miles")