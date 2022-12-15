curr = {}
l = 0

line = open('2022/6/input.txt', 'r').read().splitlines()[0]

for r in range(len(line)):
    curr[line[r]] = curr.get(line[r], 0) + 1
    if r - l + 1 > 14:
        curr[line[l]] -= 1
        if curr[line[l]] == 0:
            del curr[line[l]]
        l += 1
    if len(curr) > 13:
        print(r + 1)
        break