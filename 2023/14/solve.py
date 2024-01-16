from typing import List, Tuple

def parse(inp: str) -> List:
    """Parsing Function"""
    return [list(i) for i in open(inp, "r", encoding="utf-8").read().splitlines()]

def rocks(inp: List, rock: str) -> List:
    """Function to find indices of rocks of specified type"""
    return [index for index in range(len(inp)) if inp[index] == rock]

def column(inp: List) -> int:
    """Function to aggregate rock weight in a single column"""
    cubes = [-1]
    cubes.extend(rocks(inp, "#"))
    spheres = rocks(inp, "O")
    return recur(cubes, spheres, len(inp))

def recur(cubes: List, spheres: List, top: int) -> int:
    """Function to recursively add up rocks per buildup"""
    if not spheres:
        return 0

    total = 0
    og = len(spheres)
    while spheres and spheres[-1] > cubes[-1]:
        total += top - cubes[-1] - (og - len(spheres) + 1)
        spheres.pop()
    return total + recur(cubes[:-1], spheres, top)

def roll(sphere: Tuple, inp: List, move: Tuple) -> Tuple:
    """Function to slide-roll a spherical rock"""
    moves = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    if inp[sphere[0]][sphere[1]] == "O": #check for collision
        move = (move[0] if not move[0] else move[0] * -1, move[1] if not move[1] else move[1] * -1)
        while True:
            if inp[sphere[0]][sphere[1]] != "O":
                return sphere
            sphere = (sphere[0] + move[0], sphere[1] + move[1])


    predict = (sphere[0] + move[0], sphere[1] + move[1])
    while True:
        predict = (sphere[0] + move[0], sphere[1] + move[1])
        if -1 == predict[0] or predict[0] == len(inp) or -1 == predict[1] or predict[1] == len(inp[0]) or inp[predict[0]][predict[1]] in "#O":
            break
        sphere = predict

    return sphere

print(roll((0, 2), [['.', '.', '.']], (0, -1)))

print(roll(
    (1, 3),[
        [".", ".", ".", ".", "O", "#", ".", ".", ".", "."],
        [".", ".", "O", "O", "#", ".", ".", ".", ".", "#"],
        [".", ".", ".", ".", ".", "#", "#", ".", ".", "."],
        [".", ".", ".", "#", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "#", "."],
        [".", ".", "#", ".", ".", ".", ".", "#", ".", "#"],
        [".", ".", ".", ".", ".", "#", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["#", ".", ".", ".", ".", "#", "#", "#", ".", "."],
        ["#", ".", ".", ".", ".", "#", ".", ".", ".", "."],
    ],(0, 1)
))


def tracking(inp: List) -> int:
    """Return the number of spheres in a matrix"""
    return sum(1 for r in range(len(inp)) for c in range(len(inp[0])) if inp[r][c] == "O")

def gravitation(spheres: List, inp: List, move: Tuple) -> List:
    """Function to apply gravitation to a bunch of spherical rocks"""
    for sphere in spheres:
        r, c = roll(sphere, inp, move)
        if inp[r][c] == "O":
            print("Bad")
            print(sphere, inp, move)
        inp[r][c] = "O"
    return inp

def wipe(inp: List) -> List:
    """Wipe rocks from de matrix"""
    return [list("." if inp[r][c] == "O" else inp[r][c] for c in range(len(inp[0]))) for r in range(len(inp))]

def cycle(inp: List, cycles: int) -> List:
    """Function to put the matix through the dryer"""
    moves = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    for _ in range(cycles):
        pre_check = inp
        for move in moves:
            spheres = [(r, c) for r in range(len(inp)) for c in rocks(inp[r], "O")]
            inp = gravitation(spheres, wipe(inp), move)
        if inp == pre_check:
            for row in inp:
                print(row)
            return inp


    return inp

def a(inp: str) -> int:
    """Solution to part A"""
    return sum(column(col) for col in zip(*parse(inp)))

def b(inp: str) -> int:
    """Solution to part B (hopefully :)"""
    parsed = parse(inp)
    washed_n_dried = cycle(parsed, 1000000000)
    return sum(column(col) for col in zip(*washed_n_dried))

print(a('0'))
print(b('1'))
