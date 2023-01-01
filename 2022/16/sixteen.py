from re import findall
from dataclasses import dataclass
from typing import List
from collections import deque


i_n = list(list(int(i) if ord(i[0]) >= 48 and ord(i[0]) <= 57 else i for i in findall(r"-?\d+|[A-Z]{2}", l)) for l in open('2022/16/input.txt').read().splitlines())

@dataclass
class Neighbor:
    name: str
    distance: int 
    
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


def dijkstras(current_valve, target_valve, valid_valves):
    queue_neighbor_list = {current_valve : Neighbor(current_valve, 0)}
    queue = deque([current_valve])

    # print(queue.popleft())
    visited = set()
    while queue:
        for index in range(len(queue)):
            current = queue.popleft()
            current_neighbor = queue_neighbor_list.pop(current)
            visited.add(current)
            # when we pop a node, we add to visited. That way we can still reconfigure neigbors based on new paths, but once we're on the node it no longer can be reconfigured

            # check if dest.
            if current == target_valve:
                return current_neighbor.distance

            add_to_queue = list(Neighbor(neighbor.name, neighbor.distance + current_neighbor.distance) for neighbor in valid_valves[current].neighbors)
            # queue.extend(Neighbor(neighbor.name, neighbor.distance + current.distance) for neighbor in valid_valves[current.name].neighbors) # need to modify this so that we can add the current valves length to the length of the item in queue -> to get a valid priority queue - done.
            for neighbor in add_to_queue:
                if queue_neighbor_list.get(neighbor.name) == None and neighbor.name not in visited:
                    queue_neighbor_list[neighbor.name] = neighbor
                    queue.append(neighbor.name)
                elif queue_neighbor_list.get(neighbor.name) != None:
                    queue_neighbor_list[neighbor.name] = neighbor if neighbor.distance < queue_neighbor_list[neighbor.name].distance else queue_neighbor_list[neighbor.name]
            queue = deque(sorted(queue, key=lambda neighbor: queue_neighbor_list[neighbor].distance))

            ## need to remove possible duplicates, keeping shortest
            ## then check if destination.
            ## we also need a visited I think, to store where we came from so we don't go b ack.

def calculate_estimate(current_valve, valid_valves):
    estimated_values = {}
    for valve in valid_valves.keys():
        if valve != current_valve:
            distance = dijkstras(current_valve, valve, valid_valves)
            estimated_values[valve] = (30 - (distance + 1) ) * valid_valves[valve].flow_rate
    return estimated_values


un_weighted = convert_to_map(i_n)
valid_valves = convert_to_weighted(i_n, un_weighted)
for valve in valid_valves.keys():
    print(valid_valves[valve])

# print(valid_valves['AA'].neighbors)
print(dijkstras('AA', 'HH', valid_valves))
print(calculate_estimate('AA', valid_valves))

