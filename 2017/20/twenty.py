from dataclasses import dataclass
from copy import deepcopy
from re import findall

@dataclass
class Vertex:
    x: int
    y: int
    z: int

@dataclass
class Particle:
    pos: Vertex
    veloc: Vertex
    accel: Vertex
    name: int

input = list(findall('-?\d+', i) for i in open('input.txt').read().splitlines())
particles = list(Particle(Vertex(*map(int, [x for x in input[i][0:3]])), Vertex(*map(int, [x for x in input[i][3:6]])), Vertex(*map(int, [x for x in input[i][6:9]])), i) for i in range(len(input)))

def traverse(collision, particles, iterations):
    if collision: collisions = {}
    for i in range(0, iterations):
        for par in particles:
            par.veloc = Vertex(par.veloc.x + par.accel.x, par.veloc.y + par.accel.y, par.veloc.z + par.accel.z)
            par.pos = Vertex(par.pos.x + par.veloc.x, par.pos.y + par.veloc.y, par.pos.z + par.veloc.z)
            if collision: collisions[str(par.pos)] = collisions.get(str(par.pos), 0) + 1
        if collision:
            new = []
            for index in range(len(particles)):
                if collisions.get(str(particles[index].pos)) < 2:
                    new.append(particles[index])
            particles = new
    return particles


def brute(particles, iterations):
    return min(traverse(False, deepcopy(particles), iterations), key=lambda i: abs(i.pos.x) + abs(i.pos.y) + abs(i.pos.z)).name

def collidascope(particles, iterations):
    return len(traverse(True, deepcopy(particles), iterations))

print(brute(particles, 1000))
print(collidascope(particles, 1000))
