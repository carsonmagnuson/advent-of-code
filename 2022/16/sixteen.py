from re import findall

i_n = list(list(int(i) if ord(i[0]) >= 48 and ord(i[0]) <= 57 else i for i in findall(r"-?\d+|[A-Z]{2}", l)) for l in open('2022/16/input.txt').read().splitlines())




# print(i_n[0][1] + 2)
# print(i_n)

class Neighbor:
    
    def __init__(self, distance, name):
        self.name = name
        self.distance = distance

class Valve:
     
    def __init__(self, name, neighbors, flowrate):
        self.name = name
        self.neighbors = neighbors
        self.flow_rate = flowrate

    def __str__(self):
        return f"{self.name} ({self.flow_rate})"
    
    def __repr__(self):
        return self.__str__()
     

def get_neighbors(input, valve, valves, count, visited):
    visited.add(valve[0])
    weighted_neighbors = []
    for neighbor_index in range(2, len(valve)):
        if valve[neighbor_index] not in visited:
            if valves.get(valve[neighbor_index]) != None:
                weighted_neighbors.append(Neighbor(count, valve[neighbor_index]))
            else:
                weighted_neighbors.extend(get_neighbors(input, valve[neighbor_index], valves, count + 1, visited)) 
    return weighted_neighbors
        

def convert_to_map(input):
    connections = {}
    for valve in input:
        connections[valve[0]] = valve[2:len(valve)]
    return connections


def convert_to_weighted(input):

    valves = {}
    for valve in input:
        if valve[1] > 0 or valve[0] == "AA":
            newValve = Valve(valve[0], [], valve[1])
            valves[newValve.name] = newValve
    
    print(get_neighbors(i_n, i_n[0], valves, 1, set()))

    # for valve in valves.keys():
    #     get_neighbors()
    return valves


print(convert_to_map(i_n))
# valves = convert_to_weighted(i_n)
# valves['BB'].neighbors += 
# print(valves)

