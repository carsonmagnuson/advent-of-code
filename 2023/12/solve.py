from typing import List


def parse(inp: str) -> List[tuple[str, List[int]]]:
    """Parsing function"""
    return [(conditions, list(map(int, info.split(',')))) for conditions, info in [line.split() for line in open(inp, 'r', encoding='utf-8').read().splitlines()]]

def perms(perm: str, info: List[int]) -> int:
    """Permutations counting function"""
    if perm == "": return 1 if info == [] else 0
    if info == []: return 0 if "#" in perm else 1

    count = 0

    if perm[0] in ".?": count += perms(perm[1:], info)
    
    if perm[0] in "#?":
        if len(perm) >= info[0] and "." not in perm[:info[0]]: # check perm length is bigger than next set and that set's worth of characters are all not for sure functional
            if info[0] == len(perm) or perm[info[0]] != "#": # check that either length of perm = next set amount or that char after sets last char is functional
                count += perms(perm[info[0]+1:], info[1:])

    return count

def a(inp: str) -> int:
    """Solution to part A"""
    parsed = parse(inp)
    return sum(perms(perm, info) for perm, info in parsed)

print(a("input.txt"))
