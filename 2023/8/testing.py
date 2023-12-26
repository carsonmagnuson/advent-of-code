import re
import math
i = open('input.txt').read().splitlines()

nodes = {}
starts = []
directions = i[0].strip()
go = {'L':0, 'R':1}

for index, line in enumerate(i[2:]):
    capitals = ''.join(re.findall(r'[A-Z0-9]', line))
    nodes[capitals[0:3]] = (capitals[3:6], capitals[6:9])
    if capitals[2] == 'A':
        starts.append(capitals[0:3])



loops = []
for start in starts:
    fork = 1
    loop = 1
    tracking = {}
    curr = start
    leash = -1
    while True:
        if curr[2] == 'Z':
            print('tail found')
            leash = fork - 1
            print(leash)
            break


        curr = nodes[curr][go[directions[fork%len(directions)-1]]]
        fork += 1


    curr = nodes[curr][go[directions[fork%len(directions)-1]]]
    fork += 1

    while True:
        if curr[2] == 'Z':
            print('loop len found')
            loop = fork - (leash + 1)
            print(loop)
            break

        curr = nodes[curr][go[directions[fork%len(directions)-1]]]
        fork += 1

    loops.append((leash, loop))

print(loops)

## 10668805667831

for index in range(len(loops)):
    rem, mod = loops[index]
    if rem == mod:
        loops[index] = (0, loops[index][1])
print(loops)

lcm = loops[0][1]
curr = loops[0][0] + lcm
for index in range(1, len(loops)):
    rem, modulon = loops[index]

    while curr % modulon != rem:
            curr += lcm

    lcm =  min(lcm, modulon) // math.gcd(lcm, modulon) * max(lcm, modulon)

print(curr)

    



