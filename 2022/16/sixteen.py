from re import findall
from dataclasses import dataclass
from typing import List


i_n = list(list(int(i) if ord(i[0]) >= 48 and ord(i[0]) <= 57 else i for i in findall(r"-?\d+|[A-Z]{2}", l)) for l in open('2022/16/input.txt').read().splitlines())




# print(i_n[0][1] + 2)
# print(i_n)

@dataclass
class Neighbor:
    name: str
    distance: int 
    #def __init__(self, distance, name):
        #self.name = name
        #self.distance = distance

@dataclass
class Valve:
    name: str
    neighbors: List[Neighbor] 
    flow_rate: int
     
def get_valid_neighbors(visited, current_valve, all_valves, valid_valves, count):
    visited.add(current_valve)
    valid_neighbors = []
    for neighbor in all_valves[current_valve]:
        if neighbor not in visited:
            if valid_valves.get(neighbor) != None:
                valid_neighbors.append(Neighbor(neighbor, count))
            else:
                valid_neighbors.extend(get_valid_neighbors(visited, neighbor, all_valves, valid_valves, count + 1))
    return valid_neighbors





# def get_neighbors(input, valve, valves, count, visited):
#     visited.add(valve[0])
#     weighted_neighbors = []
#     for neighbor_index in range(2, len(valve)):
#         if valve[neighbor_index] not in visited:
#             if valves.get(valve[neighbor_index]) != None:
#                 weighted_neighbors.append(Neighbor(count, valve[neighbor_index]))
#             else:
#                 weighted_neighbors.extend(get_neighbors(input, valve[neighbor_index], valves, count + 1, visited)) 
#     return weighted_neighbors
        

def convert_to_map(input):
    connections = {}
    for valve in input:
        connections[valve[0]] = valve[2:len(valve)]
    return connections


def convert_to_weighted(input, all_valves):
    valid_valves = {}
    for valve in input:
        if valve[1] > 0 or valve[0] == "AA":
            newValve = Valve(valve[0], [], valve[1])
            valid_valves[newValve.name] = newValve
    for valve in valid_valves.keys():
        valid_valves[valve].neighbors = get_valid_neighbors(set(), valve, all_valves, valid_valves, 1)
    return valid_valves


un_weighted = convert_to_map(i_n)
valid_valves = convert_to_weighted(i_n, un_weighted)
for valve in valid_valves.keys():
    print(valid_valves[valve])

# print(get_valid_neighbors(set(), 'BB', un_weighted, valid_valves, 1))

# valves = convert_to_weighted(i_n)
# valves['BB'].neighbors += 
# print(valves)

