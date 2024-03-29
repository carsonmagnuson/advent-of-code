import re
import math
i = open('input2.txt').read().splitlines()

nodes = {}
starts = []
directions = i[0].strip()

for index, line in enumerate(i[2:]):
    capitals = ''.join(re.findall(r'[A-Z0-9]', line))
#r'[A-Z]'
    nodes[capitals[0:3]] = (capitals[3:6], capitals[6:9])
    if capitals[2] == 'A':
        starts.append(capitals[0:3])

#place = 'AAA'
#moves = 1
go = {'L':0, 'R':1}
#while place != 'ZZZ':
#    curr = directions[moves%len(directions)-1]
#    place = nodes[place][go[curr]]
#    moves += 1


#moves = 1
#while set(i[2] for i in starts) != set(['Z']):

#    curr = directions[moves%len(directions)-1]
#    for index, start in enumerate(starts):
#        starts[index] = nodes[start][go[curr]]
#    moves += 1

#print(moves-1)


loops = []
for start in starts:
    tracking = {}
    curr = start
    fork = 1
    loop = 1
    leash = -1
    while True:
        if tracking.get(curr):
            if leash != -1:
                loops.append((leash, loop - tracking[curr]))
                break 
            else:
                print('rodeled')
                loop = tracking[curr]
        else:
            tracking[curr] = loop

        if curr[2] == 'Z':
            print('tail found')
            leash = fork - 1
            loop = tracking[curr]


        curr = nodes[curr][go[directions[fork%len(directions)-1]]]
        fork += 1
        loop += 1


print(loops)

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
    

## 10668805667831

     
