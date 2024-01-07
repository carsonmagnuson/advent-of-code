from collections import deque

def p(input):
    input = [list(i) for i in open(input, 'r').read().splitlines()]
    return input

def s(input):
    s = 0
    for index in range(len(input)):
        if 'S' in input[index]:
            s = (index, input[index].index('S'))
    return s

def m(input, start):
    moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    check = {'S': moves, '-': moves[::3], '|': moves[1:3], 'L': moves[::2], 'J': moves[2:], '7': moves[1::2], 'F': moves[:2]}
    valid = {'(0, 1)':['-', '7', 'J'], '(1, 0)':['|', 'L', 'J'], '(-1, 0)': ['|', '7', 'F'], '(0, -1)':['-', 'L', 'F']}

    q = deque([(start, 0)])

    while q:
        curr = q.popleft()
        step = curr[1]
        r, c = curr[0]
        if type(input[r][c]) == str:
            for x, y in check[input[r][c]]:
                r_, c_ = r + x, c + y

                if input[r_][c_] in valid[str((x, y))]:
                    
                    q.append(((r_, c_), step + 1))
            input[r][c] = step

    return input 

def i(input):
    intervals = []

    start, end = -1, -1

    for index in range(len(input)):
        if type(input[index]) == int:
            if start == -1:
                start = index
            end = index
        elif start != -1:
            intervals.append((start, end))
            start, end = -1, -1
    if start != -1:
        intervals.append((start, end))    

    return intervals


def v(input, start):
    moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    check = {'S': moves, '-': moves[::3], '|': moves[1:3], 'L': moves[::2], 'J': moves[2:], '7': moves[1::2], 'F': moves[:2]}
    valid = {'(0, 1)':['-', '7', 'J'], '(1, 0)':['|', 'L', 'J'], '(-1, 0)': ['|', '7', 'F'], '(0, -1)':['-', 'L', 'F']}
    vertices = []
    r, c = start
    while True:
        vertices.append((r, c))
        for x, y in check[input[r][c]]:
            if input[r + x][c + y] in valid[str((x, y))]:
                input[r][c] = 0
                r = r + x
                c = c + y
                break
        if (r, c) == vertices[-1]:
            break

    return vertices

def shoelace(vertices):
    l, r = 0, 0
    for index, vertex in enumerate(vertices):
        l += vertex[0] * vertices[((index + 2) % len(vertices)) -1][1]
        r += vertex[1] * vertices[((index + 2) % len(vertices)) -1][0]
    return abs(l-r)//2

def a(input):
    input = p(input)
    input = m(input, s(input))

    return max([el if type(el) == int else 0 for line in input for el in line])

def b(input):
    input = p(input)
    start = s(input)
    vertices = v(input, start)
    shoe = shoelace(vertices)
    modif_pick = int(shoe + 1 - (0.5*(len(vertices))))
    return  modif_pick

print(b('input.txt'))
