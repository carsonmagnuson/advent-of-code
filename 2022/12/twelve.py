

## okay so I need to traverse a depth map by from a start point 
# in step increments of one and only to depths + 1 of my currrent depth or lower to find a destination.
# And I have no clue what the optimal solution is.
# Okay so we're in agreement. Recursive brute-force algorithm.
# Okay so the recursive depth-first brute-force algorithm is too slow. We're gonna try
# the A* thingy. Okay so A* wasn't the actual thing, it's BFS that we needed, and queue. Much less intuitive to me than DFS and recursion.


from collections import deque, defaultdict
iN, start, end, results, moves = list(list(ord(c) - 97 for c in list(l)) for l in (line.rstrip() for line in open('2022/12/input.txt'))), [], [], [], [(0,1), (0, -1), (1, 0), (-1, 0)]
print('Salutations, my goodman. Assembling your answer now...')

for y, line in enumerate(iN):
    for x, depth in enumerate(line):
        if depth == -14 or depth == 0: start, iN[y][x] = start + [[x, y]], 0
        elif depth == -28: end, iN[y][x] = [x,y], 25

for p in start:
    visited, count, q, done = set(), 0, deque([p]), False
    while q and not done:
        for index in range(len(q)):
            p = q.pop()
            if p == end: done = True and results.append(count)
            if done: break
            for x, y in moves:
                n = [p[0] + x, p[1] + y]
                if n[0] > 0 and n[0] < (len(iN[0])) and n[1] > 0 and n[1] < (len(iN)) and str(n[0]) + ' ' + str(n[1]) not in visited and (iN[n[1]][n[0]] - iN[p[1]][p[0]]) < 2: visited.add(str(n[0]) + " " + str(n[1])), q.appendleft(n)
        count += 1

print(sorted(results)[0])


# while q and not done:
#     for index in range(len(q)):
#         p = q.pop()
#         if p == end:
#             results.append(count)
#             done = True
#             break
            
#         up = [p[0], p[1] - 1]
#         s = str(up[0]) + ' ' + str(up[1])
#         if p[1] > 0 and s not in visited and (iN[up[1]][up[0]] - iN[p[1]][p[0]]) < 2:
#             visited.add(str(up[0]) + " " + str(up[1]))
#             q.appendleft(up)
        
#         right = [p[0] + 1, p[1]]
#         s = str(right[0]) + ' ' + str(right[1])
#         if p[0] < (len(iN[0]) - 1) and s not in visited and (iN[right[1]][right[0]] - iN[p[1]][p[0]]) < 2:
#             visited.add(str(right[0]) + " " + str(right[1]))
#             q.appendleft(right)
        
#         down = [p[0], p[1] + 1]
#         s = str(down[0]) + ' ' + str(down[1])
#         if p[1] < (len(iN) - 1) and s not in visited and (iN[down[1]][down[0]] - iN[p[1]][p[0]]) < 2:
#             visited.add(str(down[0]) + " " + str(down[1]))
#             q.appendleft(down)

#         left = [p[0] - 1, p[1]]
#         s = str(left[0]) + ' ' + str(left[1])
#         if p[0] > 0 and s not in visited and (iN[left[1]][left[0]] - iN[p[1]][p[0]]) < 2:
#             visited.add(str(left[0]) + " " + str(left[1]))
#             q.appendleft(left)
#     count += 1
        





# def r(p, end, count, visited): ## four options, always. Wait, but we don't want to go backwards, that could lead to a never ending loop
#     ## remember to check for if-end
#     s = str(p[0]) + ' ' + str(p[1])
#     visited.add(s)
#     # print(count)
#     if p == end:
#         results.append(count)
#         return

#     right = [p[0] + 1, p[1]]
#     s = str(right[0]) + ' ' + str(right[1])
#     if p[0] < (len(iN[0]) - 1):
#         if s not in visited and (iN[right[1]][right[0]] - iN[p[1]][p[0]]) < 2:
#             r(right, end, count + 1, visited.copy())
    
#     left = [p[0] - 1, p[1]]
#     s = str(left[0]) + ' ' + str(left[1])
#     if p[0] > 0 and s not in visited and (iN[left[1]][left[0]] - iN[p[1]][p[0]]) < 2:
#         r(left, end, count + 1, visited.copy())

#     up = [p[0], p[1] - 1]
#     s = str(up[0]) + ' ' + str(up[1])
#     if p[1] > 0 and s not in visited and (iN[up[1]][up[0]] - iN[p[1]][p[0]]) < 2:
#         r(up, end, count + 1, visited.copy())
    
#     down = [p[0], p[1] + 1]
#     s = str(down[0]) + ' ' + str(down[1])
#     if p[1] < (len(iN) - 1) and s not in visited and (iN[down[1]][down[0]] - iN[p[1]][p[0]]) < 2:
#         r(down, end, count + 1, visited.copy())

# r(start, end, 0, set())
# print(sorted(results)[0])
