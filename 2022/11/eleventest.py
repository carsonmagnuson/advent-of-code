## monkey business pt 2–this is disgusting, I know, don't ask. I had no clue past simplifying with the mod how to figure stuff out, so I used data structure hacks
import re
import math
from collections import deque, defaultdict

print('Salutations, my goodman. Crutch code in progress...')
l, o, mS, c = list(li for li in (l.rstrip() for l in open('2022/11/input.txt')) if li), {'*': lambda oR, n, mO: (oR * (int(n) if n != 'old' else oR)) % mO, '+': lambda oR, n, mO: (oR + (int(n) if n != 'old' else oR) % mO)}, defaultdict(list), len(open('2022/11/input.txt').read().split('\n\n'))
for i, li in enumerate(l): mS[int(li.split()[1][0])].extend((deque(list(map(list,zip(*list(list(map(int, re.findall('\d+', l[i + 1]))) for _ in range(c)))))), l[i + 2].split()[-2:], list(map(int, list(l[i + x].split()[-1] for x in range(3, 6)))), 0)) if li[0] != ' ' else () 
for r in range(0, 10000):
    for m in mS.keys():
        for i in range(len(mS.get(m)[0])):
            for x in range(c): mS[m][0][0][x] = o[mS.get(m)[1][0]](mS[m][0][0][x], mS.get(m)[1][1], mS.get(x)[2][0])
            mS[mS.get(m)[2][1]][0].append(mS[m][0].popleft()) if mS[m][0][0][m] % mS.get(m)[2][0] == 0 else mS[mS.get(m)[2][2]][0].append(mS[m][0].popleft())
            mS[m][3] += 1
print(math.prod(sorted(list(mS[x][3] for x in range(0, len(mS))))[-2:]))