from typing import List


def parse(inp: str) -> List:
    """Parsing Function"""
    return [
        list(list(line) for line in i.rstrip().split("\n")) for i in open(inp, "r", encoding="utf-8").read().split("\n\n")
    ]

def mirrorline(inp: List) -> int:
    """Function to identify mirrorline if exists else returns 0"""

    for x in range(2):
        if x:
            inp = list(zip(*inp))

        potentials = [index for index in range(len(inp) - 1) if inp[index] == inp[index + 1]]

        for potential in potentials:
            spacer = 3
            bad = False
            p_index = potential-1
            while p_index > -1 and p_index + spacer < len(inp):
                if inp[p_index] != inp[p_index + spacer]:
                    bad = True
                    break
                spacer += 2
                p_index -= 1

            if not bad:
                return potential + 1 if x else (potential + 1)*100

    print('bad')
    return 0

def diff(l: List, r: List) -> int:
    """Function to return how many elements are diff between two lists"""
    return sum(1 for index in range(len(l)) if l[index] != r[index])

def ripple(inp: List, drop: int, tolerance: int) -> bool:
    """Function to return if mirror image valid within tolerance"""
    spacer = 3
    p_index = drop - 1
    while p_index > -1 and p_index + spacer < len(inp):
        differ = diff(inp[p_index], inp[p_index + spacer])
        if differ == 1:
            if tolerance:
                tolerance -= 1
            else:
                return False
        if differ > 1:
            return False
        spacer += 2
        p_index -= 1

    return not tolerance    

def smudge(inp: List) -> int:
    """Function to find smudged mirrorline"""
    vertical = 0
    original = mirrorline(inp)
    if original < 100:
        vertical = 1
    avoid = original%100 - 1

    for orientation in range(2):
        if orientation:
            inp = list(zip(*inp))

        for index, line in enumerate(inp[:-1]):
            differ = diff(line, inp[index + 1])
            if not differ and (index != avoid or orientation != vertical):
                if ripple(inp, index, 1):
                    return index + 1 if orientation else (index + 1) * 100
            if differ == 1:
                if ripple(inp, index, 0):
                    return index + 1 if orientation else (index + 1) * 100

    print('bad')
    return 0

def a(inp: str) -> int:
    """Solution to part A"""
    return sum(mirrorline(mirror) for mirror in parse(inp))

def b(inp: str) -> int:
    """Solution to part B"""
    return sum(smudge(mirror) for mirror in parse(inp))

print(a('0'))
print(b('0'))

