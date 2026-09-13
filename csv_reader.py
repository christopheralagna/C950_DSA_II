import csv
from HashTable import HashTable
from Package import Package

def load_package_data(filename: str, hash_table: HashTable) -> None:
    with open(filename, 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            if not row or row[0] == "Package ID":
                continue
            
            package_id = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip_code = row[4]
            delivery_deadline = row[5]
            weight = int(row[6])
            special_notes = row[7]

            package = Package(package_id, address, city, state, zip_code, delivery_deadline, weight, special_notes)
            hash_table.insert_package(package)