import csv
from hash_table import HashTable
from package import Package

#loads package data from CSV into hash table
def load_package_data(filename: str, hash_table: HashTable) -> None:
    with open(filename, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)

        for row in reader:
            #skip empty rows or header row
            if not row or "Package ID" in row[0]:
                continue
            
            #extract data from each row
            package_id = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip_code = row[4]
            delivery_deadline = row[5]
            weight = int(row[6])
            special_notes = row[7]

            #create package object and insert into hash table
            package = Package(package_id, address, city, state, zip_code, delivery_deadline, weight, special_notes)
            hash_table.insert_package(package)

def load_distance_data(filename: str):
    address_map = {}
    distance_matrix = []
    index = 0

    with open(filename, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        for row in reader:
            if not row:
                continue

            # Create an address map with first element of each row being the key, index being value
            address = row.pop(0)
            address_map[address] = index
            index += 1

            # Create distance matrix with distances from each address
            distances = []
            for val in row:
                if val != "":
                    distances.append(float(val))
            distance_matrix.append(distances)

    return address_map, distance_matrix