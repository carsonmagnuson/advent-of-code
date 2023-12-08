import re
i = open('test3.txt').read().splitlines()

nodes = {}
directions = i[0].strip()
print(directions)

for line in i[2:]:
    capitals = ''.join(re.findall(r'[A-Z]', line))
    nodes[capitals[0:3]] = (capitals[3:6], capitals[6:9])

place = 'AAA'
moves = 1
go = {'L':0, 'R':1}
while place != 'ZZZ':
    curr = directions[moves%len(directions)-1]
    place = nodes[place][go[curr]]
    moves += 1

print(moves-1)

