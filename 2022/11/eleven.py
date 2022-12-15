## monkey business
import re
from collections import deque
lines = list(line for line in (l.rstrip() for l in open('2022/11/input.txt')) if line)

# operations = {'*': lambda orig, new, mod: (orig * (int(new) if new != 'old' else orig)) % mod, '+': lambda orig, new, mod: (orig + (int(new) if new != 'old' else orig) % mod)}
monkes = {}
for index, line in enumerate(lines):
    if line[0] != ' ':
        currMonke = int(line.split()[1][0])
        monkes[currMonke] = []

        items = deque(map(int, re.findall('\d+', lines[index + 1])))
        monkes[currMonke].append(items)

        operation = lines[index + 2].split()[-2:]
        monkes[currMonke].append(operation)

        test = list(map(int, list(lines[index + x].split()[-1] for x in range(3, 6))))
        monkes[currMonke].append(test)

        inspections = 0
        monkes[currMonke].append(inspections)

for round in range(0, 20):
    for currMonke in monkes.keys():
        for i in range(len(monkes.get(currMonke)[0])):
            operation, by = monkes.get(currMonke)[1]
            mod = monkes.get(currMonke)[2][0]
            # monkes[currMonke][0][0] = operations[operation](monkes[currMonke][0][0], by, monkes.get(currMonke)[2][0])  # inspection
            if operation == '+':
                monkes[currMonke][0][0] = ((monkes[currMonke][0][0]) + (int(by)) if by != 'old' else (monkes[currMonke][0][0]) + (monkes[currMonke][0][0])) // 3
            else:
                monkes[currMonke][0][0] = ((monkes[currMonke][0][0]) * (int(by)) if by != 'old' else (monkes[currMonke][0][0]) * (monkes[currMonke][0][0])) // 3
            
            # if monkes[currMonke][0][0] >= 10:
            #     monkes[currMonke][0][0] -= 10
                
            # monkes[currMonke][0][0] = monkes[currMonke][0][0] % 10
            monkes[currMonke][3] += 1
            if monkes[currMonke][0][0] % mod == 0:
                destination = monkes.get(currMonke)[2][1]
                monkes[destination][0].append(monkes[currMonke][0].popleft())
            else:
                destination = monkes.get(currMonke)[2][2]
                monkes[destination][0].append(monkes[currMonke][0].popleft())




simianshenanigans = sorted(list(monkes[x][3] for x in range(0, len(monkes))))
monkebusiness = simianshenanigans[-1] * simianshenanigans[-2]
print(simianshenanigans)

print(monkebusiness)
                
## I solved pt 1, however, for pt 2 the numbers get too big and the rounds too many for my algorithm to handle.
# It would take forever for it to solve 10,000 rounds, so I have to figure out a different solution. If I look
# at the number of inspections from round to round they increment in some sort of pattern, so maybe I'll start
# there.
## okay monkey 3 is incrementing in an interesting pattern, 4-7

# def modding(num): ## 8 and 5 don't seem to work as a test case in multiplication
#     return num % 5

# num1, num2 = 9939, 85858392
# print((num1+num2) % 5)
# print((modding(num1) + modding(num2)) % 5)



