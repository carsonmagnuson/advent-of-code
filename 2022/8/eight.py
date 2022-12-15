## okay so we're given a grid of numbers, and we need to to find 
# the total amount of numbers that have some ajdacent line of 
# numbers to an edge of the gride that are all lower, aka a 'tree'
# that is 'visible' from the outside.

#if we hit 9 from a certain direction, we know that no more trees 
# will be visible from that outside vector.
# brute force solution idea is to iterate the array from each direction
# and store higher nums as their coordinate in a set until we hit 
# nine or the end of the line, then return that.

from collections import deque 
i, m, ts, v = open('2022/8/input.txt', 'r').read().splitlines(), [], set(), {}
for x in i:
    m.append(list(map(int, list(x))))
for y, l in enumerate(m):
    p, b = deque(), -1
    for x, t in enumerate(l):
        if x == 0: v[str(x) + " " + str(y)] = 0
        else:
            while len(p) != 0 and p[-1][0] < t: p.pop()
            v[str(x) + " " + str(y)] = x if len(p) == 0 else x - p[-1][1]
        p.append([t, x])
        if t > b: ## hashing coords for pt 1
            ts.add(str(x) + " " + str(y))
            b = t
for y, l in enumerate(m):
    p, b = deque(), -1
    for x, t in reversed(list(enumerate(l))):
        if x != 4: ## assigning scenic value for pt 2
            while len(p) != 0 and p[-1][0] < t: p.pop()
            v[str(x) + " " + str(y)] *= len(l) - 1 - x if len(p) == 0 else p[-1][1] - x
        else: v[str(x) + " " + str(y)] = 0
        p.append([t, x])
        if t > b: ## hashing coords for pt 1
            ts.add(str(x) + " " + str(y))
            b = t
for x, l in enumerate(zip(*m)):
    p, b = deque(), -1
    for y, t in enumerate(l):
        if y != 0: # assigning scenic value for pt 2
            while len(p) != 0 and p[-1][0] < t: p.pop()
            v[str(x) + " " + str(y)] *= y if len(p) == 0 else y - p[-1][1]
        else: v[str(x) + " " + str(y)] = 0
        p.append([t, y])
        if t > b: ## hashing coords for pt 1
            ts.add(str(x) + " " + str(y))
            b = t
for x, l in enumerate(zip(*m)):
    p, b = deque(), -1
    for y, t in reversed(list(enumerate(l))):
        if y != 4: ## assigning scenic value for pt 2
            while len(p) != 0 and p[-1][0] < t: p.pop()
            v[str(x) + " " + str(y)] *= len(l) - 1 - y if len(p) == 0 else p[-1][1] - y
        else:
            v[str(x) + " " + str(y)] = 0
        p.append([t, y])
        if t > b: ## hashing coords for pt 1
            ts.add(str(x) + " " + str(y))
            b = t
print(f'part 1 ans: {len(ts)}, pt 2 ans: {max(v.values())}')





## so for the second part I have to get a 'scenic value' for each
# position. I'm thinking same thing as the first problem, but now I
# use a stack to keep track of the values and their orders, and pop
# them as needed to determine a position's scenic value from one
# vector at a time

# The current issue I'm running into is that the scenic value equates
# to the number of trees you can see, so that's inclusive of the final
# tree that's bigger than you, but the edge, since it's not a tree, does 
# not count towards the scenic value. Tricky.
# y = 0
# l = [3,5,3,5,3]
# p = deque()
# for x, t in reversed(list(enumerate(l))):
#         if x == 4:
#             v[str(x) + " " + str(y)] = [0]
#         else:
#             while len(p) != 0 and p[-1][0] < t:
#                 p.pop()
#             v[str(x) + " " + str(y)] = [len(l)-1-x] if len(p) == 0 else [p[-1][1] - x]
#         p.append([t, x])

# print(v)