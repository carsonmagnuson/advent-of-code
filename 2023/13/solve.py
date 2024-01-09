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

        potentials = [
            index for index in range(len(inp) - 1) if inp[index] == inp[index + 1]
        ]

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


def a(inp: str) -> int:
    """Solution to part A"""
    return sum(mirrorline(mirror) for mirror in parse(inp))

print(a('0'))

