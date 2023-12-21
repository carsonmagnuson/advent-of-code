import re
i = open('test3.txt').read().splitlines()

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

first = nodes[starts[0]][go[directions[0]]]
fork = 2

while first != starts[0]:
    curr = directions[fork%len(directions)-1]
    first = nodes[first][go[curr]]
    fork += 1
    print(first)
    print(starts[0])
print(fork)

     
