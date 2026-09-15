
from __future__ import annotations
from package import Package

class HashTable:

    #initialize hash table. Use 10 inner lists for the buckets. Hash collisions handled by separate chaining.
    def __init__(self, initial_capacity:int = 10) -> None:
        self.table: list[list[Package]] = [[] for _ in range(initial_capacity)]

    #hash function using modulo operator and length of table (10)
    def hash(self, package_id: int) -> int:
        return package_id % len(self.table)
        
    #insert package into hash table. Checks if package already exists and updates if it does.
    def insert_package(self, package: Package) -> None:
        bucket = self.table[self.hash(package.package_id)]

        for i in range(len(bucket)):
            if bucket[i].package_id == package.package_id:
                bucket[i] = package
                return

        #apply special notes if applicable
        if package.package_id in [3, 18, 36, 38]:
            package.special_notes = "Must be on truck 2"
        elif package.package_id in [6, 25, 28, 32]:
            package.special_notes = "delayed on flight until 9:05 am"
        elif package.package_id == 14:
            package.special_notes = "Must be delivered with 15 and 19"
        elif package.package_id == 16:
            package.special_notes = "Must be delivered with 13 and 19"
        elif package.package_id == 20:
            package.special_notes = "Must be delivered with 13 and 15"
        elif package.package_id == 9:
            package.special_notes = "Wrong Address. Correct Address will be updated at 10:20 am."
            
        bucket.append(package)

    #search for package by package id. Returns package if found, None otherwise.
    def search_package(self, package_id: int) -> Package | None:
        bucket = self.table[self.hash(package_id)]

        for p in bucket:
            if p.package_id == package_id:
                return p

        return None