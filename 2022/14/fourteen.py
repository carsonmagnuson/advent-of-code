#I'm ngl this one seems tough from the start. I already am not sure how to approach this. I'm guessing I'll just make a matrix and plot the lines acording to input and see what that looks like. It looks like the bounds are around 450-600ish

from collections import defaultdict

i_n, dwayne_j =  list(list(list(int(n) for n in c.strip().split(',')) for c in l.split('->'))for l in open('2022/14/input.txt').read().splitlines()), []
print('Salutations my goodman, we are crutching up the Rock as we speak..')

for y in range(0, 200):
    dwayne_j.append([])
    for x in range(0, 500):
        dwayne_j[y].append('_')

big = 0
for shelf in i_n:
    for shelf_index in range(len(shelf) - 1):
        first_point, second_point = shelf[shelf_index], shelf[shelf_index + 1]
        big = max(big, first_point[1])
        big = max(big, second_point[1])
        if first_point[0] != second_point[0]:
            positive = True
            if second_point[0] - first_point[0] < 0:
                positive = False
            for x in range(first_point[0] if positive else second_point[0], second_point[0] + 1 if positive else first_point[0] + 1):
                dwayne_j[first_point[1]][x - 300] = '#'
        elif first_point[1] != second_point[1]:
            positive = True
            if second_point[1] - first_point[1] < 0:
                positive = False
            for y in range(first_point[1] if positive else second_point[1], second_point[1] + 1 if positive else first_point[1] + 1):
                dwayne_j[y][first_point[0] - 300] = '#'
            
# crutch floor fix
for x in range(len(dwayne_j[0])):
    dwayne_j[big + 2][x] = "#"

print(big)


definitely_done = False
count = 0
while not definitely_done:
    test_sandgrain = [200, 0]
    done = False
    while not done:
        if dwayne_j[test_sandgrain[1] + 1][test_sandgrain[0]] == '_':
            test_sandgrain[1] += 1
        elif dwayne_j[test_sandgrain[1] + 1][test_sandgrain[0] - 1] == '_':
            test_sandgrain[1] += 1
            test_sandgrain[0] -= 1
        elif dwayne_j[test_sandgrain[1] + 1][test_sandgrain[0] + 1] == '_':
            test_sandgrain[1] += 1
            test_sandgrain[0] += 1
        else:
            dwayne_j[test_sandgrain[1]][test_sandgrain[0]] = 'O'
            count += 1
            if test_sandgrain == [200, 0]:
                definitely_done = True
                break
            done = True
    # for x in dwayne_j:
    #     print(x)

print(count)


for x in dwayne_j:
    print(x)

