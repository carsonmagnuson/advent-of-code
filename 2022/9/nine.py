# the problem part a describes two points (H, T) on a 2D plane that are
# connected by the rule that T must always move to be adjacent to H. we
# have to track how many unique positions T ends up in following this
# rule. T is like a bodyguard lmao.
# My first inclination is to just have coordinates, that I increment,
# I don't think I really need a data structure at all here. Let's try.
# Okay we got part one. I wrote a beginning structure, then deleted it 
# all to try again, because I just hated the way it felt. Pt two is the
# same thing as pt 1 but with 10 knots instead of 1, and you're only
# tracking the last one. I'm thinking a list of lists. 
# So the list of lists worked, but the author made the movements
# annoying–because the differing knots use the head's motion as their own
# for adjustments it seems. Ok that was wrong - me, 8 hours later.

import math
iN, h, t, v, m = open('2022/9/input.txt', 'r').read().splitlines(), [0, 0], [[0, 0] for _ in range(9)], set(), {'R': lambda x, y: [x + 1, y], 'L': lambda x, y: [x - 1,y], 'U': lambda x, y: [x, y + 1], 'D': lambda x, y: [x,y - 1]}
def a(b, f):
    tMp, xD, yD = b.copy(), f[0] - b[0], f[1] - b[1] ## Alex made below line possible with leetcode magic of int
    b[0], b[1] = b[0] + int(xD / 2), b[1] + int(yD / 2) ## using int on line below–auto ceils negativs and floors positives. Noice.
    if tMp[0] != b[0] and tMp[1] == b[1]: b[1] += math.ceil(yD/2) if yD >= 0 else math.floor(yD/2)
    if tMp[1] != b[1] and tMp[0] == b[0]: b[0] += math.ceil(xD/2) if xD >= 0 else math.floor(xD/2)
    return b
for l in iN:
    for i in range(int(l.split()[1])):
        h = m[l.split()[0]](h[0], h[1])
        for j in range(len(t)):
            if j == 0: t[j] = a(t[j], h)
            else: t[j] = a(t[j], t[j - 1])
        v.add(str(t[-1][0]) + " " + str(t[-1][1]))  
print(len(v))





