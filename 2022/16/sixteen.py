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
     
def convert_to_map(input):
    connections = {}
    for valve in input:
        connections[valve[0]] = valve[2:len(valve)]
    return connections


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
    visited = set()
    while queue:
        for index in range(len(queue)):
            current = queue.popleft()
            current_neighbor = queue_neighbor_list.pop(current)
            visited.add(current)

            if current == target_valve:
                return current_neighbor.distance

            add_to_queue = list(Neighbor(neighbor.name, neighbor.distance + current_neighbor.distance) for neighbor in valid_valves[current].neighbors)
            for neighbor in add_to_queue:
                if queue_neighbor_list.get(neighbor.name) == None and neighbor.name not in visited:
                    queue_neighbor_list[neighbor.name] = neighbor
                    queue.append(neighbor.name)
                elif queue_neighbor_list.get(neighbor.name) != None:
                    queue_neighbor_list[neighbor.name] = neighbor if neighbor.distance < queue_neighbor_list[neighbor.name].distance else queue_neighbor_list[neighbor.name]
            queue = deque(sorted(queue, key=lambda neighbor: queue_neighbor_list[neighbor].distance))

def calculate_estimate(current_valve, valid_valves, time_left, visited):
    estimated_values = {}
    for valve in valid_valves.keys():
        if valve != current_valve and valve not in visited:
            distance = dijkstras(current_valve, valve, valid_valves)
            estimated_values[valve] = ((time_left - (distance + 1) ) * valid_valves[valve].flow_rate, distance) ## the magic
    return estimated_values

def determine_options(current_valve, valid_valves, minutes_left, visited):
    magic_numbers = calculate_estimate(current_valve, valid_valves, minutes_left, visited)
    ordered_options = sorted(list([key, magic_numbers[key]] for key in magic_numbers), key=lambda valve: valve[1][0], reverse=True)
    return ordered_options

    ## I have two potential approaches - depth or breadth. My paper solution went two deep each time, but idk if that's enough. Lets try it though.
 ## maybe we allow for a depth setting and a breadth setting



un_weighted = convert_to_map(i_n)
valid_valves = convert_to_weighted(i_n, un_weighted)
for valve in valid_valves.keys():
    print(valid_valves[valve])

minutes_left = 30
visited = set(['AA'])
current = 'AA'
cumulative_pressure_released = 0
pressure_rate = 0

while visited != set(valid_valves.keys()):
    options = determine_options(current, valid_valves, minutes_left, visited)
    time_taken = options[0][1][1] + 1  # the opening of the valve is + 1
    option_chosen = options[0][0]

    minutes_left -= time_taken
    visited.add(option_chosen)
    current = option_chosen
    if minutes_left < time_taken:
        cumulative_pressure_released += minutes_left * pressure_rate
    else:
        cumulative_pressure_released += time_taken * pressure_rate
    pressure_rate += valid_valves[option_chosen].flow_rate

print(cumulative_pressure_released)
print(minutes_left)
