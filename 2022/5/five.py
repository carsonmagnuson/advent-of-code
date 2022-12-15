from collections import deque, defaultdict
import re

## boolan for when we hit the second part of the input
done = False

## final boy
final = ['']*9

## stacks, ending with stack number
stacks = defaultdict(deque)

## amount, origin, destination
instructions = []

## parsing data
for line in open('2022/5/input.txt', 'r').read().splitlines():
    if line == "":
        done = True
    if not done:
        for x in range(1, len(line), 4):
            if line[x] != ' ':
                stacks[x].appendleft(line[x])
    elif line != "":
        instructions.append(re.findall('\d+', line))

## reindexing the stacks
for x in range(len(stacks.keys())):
    stacks[stacks[list(stacks.keys())[x]].popleft()] = stacks[list(stacks.keys())[x]]

## executing intructions v2
for instruc in instructions:
    temp = deque()
    for x in range(0, int(instruc[0])):
        temp.append(stacks[instruc[1]].pop())
    for x in range(0, int(instruc[0])):
        stacks[instruc[2]].append(temp.pop())
        
## joining final string
for key in stacks.keys():
    if type(key) == str:
        final[int(key)-1] = stacks[key].pop()

print(''.join(final))