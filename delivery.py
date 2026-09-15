from truck import Truck
from distances import get_distance
from datetime import datetime, timedelta

#find the package on the truck that has the shortest delivery time, move truck to that location, deliver the package, record time, repeat until all packages are delivered, return truck to hub
def deliver_packages(truck: Truck, address_map: dict[str, int], distance_matrix: list[list[float]], current_time: datetime):
    #loop until all packages are delivered
    while truck.packages:
        #update address for package 9 if current_time is at or after 10:20 am
        if current_time >= timedelta(hours=10, minutes=20):
            for package in truck.packages:
                if package.package_id == 9:
                    package.address = "410 S State St"
                    package.zip_code = "84111"

        shortest_distance = float('inf')
        shortest_delivery_package = None
        
        #loop through all packages on the truck to find closest package
        for package in truck.packages:
            distance = get_distance(truck.current_location, package.address, address_map, distance_matrix)
            if distance < shortest_distance:
                shortest_distance = distance
                shortest_delivery_package = package
            
        #calculate delivery travel time (hours to minutes)
        delivery_minutes = (shortest_distance / truck.speed) * 60
        current_time += timedelta(minutes=delivery_minutes)
        truck.mileage += shortest_distance

        #update package delivery info
        truck.current_location = shortest_delivery_package.address
        shortest_delivery_package.delivery_time = current_time
        truck.packages.remove(shortest_delivery_package)

    # Return truck to HUB
    return_distance = get_distance(truck.current_location, "HUB", address_map, distance_matrix)
    return_minutes = (return_distance / truck.speed) * 60
    current_time += timedelta(minutes=return_minutes)
    truck.mileage += return_distance
    truck.current_location = "HUB"
    return current_time
    
    
        
        
    
    
