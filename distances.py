#return distance between two addresses using address map and distance matrix
def get_distance(addr1: str, addr2: str, address_map: dict[str, int], distance_matrix: list[list[float]]) -> float:
    #get index for each address
    index_1 = address_map[addr1]
    index_2 = address_map[addr2]
    
    #return distance from distance matrix. (symmetric lookup)
    if index_1 >= index_2:
        return distance_matrix[index_1][index_2]
    else:
        return distance_matrix[index_2][index_1]
