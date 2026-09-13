
from __future__ import annotations
from Package import Package

class HashTable:

    #initialize hash table. Use 10 inner lists for the buckets. Hash collisions handled by separate chaining
    def __init__(self, initial_capacity:int = 10) -> None:
        self.table: list[list[Package]] = [[] for _ in range(initial_capacity)]

    #hash function using modulo operator and length of table (10)
    def hash(self, package_id: int) -> int:
        return package_id % len(self.table)
        
    #insert package into hash table. Check if package already exists and update if it does
    def insert_package(self, package: Package) -> None:
        bucket = self.table[self.hash(package.package_id)]

        for i in range(len(bucket)):
            if bucket[i].package_id == package.package_id:
                bucket[i] = package
                return
            
        bucket.append(package)

    #search for package by package id. Return package if found, None otherwise
    def search_package(self, package_id: int) -> Package | None:
        bucket = self.table[self.hash(package_id)]

        for p in bucket:
            if p.package_id == package_id:
                return p

        return None