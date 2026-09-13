from hash_table import HashTable
from csv_reader import load_package_data

#initialize hash table and load package data from CSV
hash_table = HashTable()
load_package_data("WGUPS_Packages.csv", hash_table)

#search for and print all packages
for i in range(1, 41):
    package = hash_table.search_package(i)
    print(package)