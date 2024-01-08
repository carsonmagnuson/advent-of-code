from typing import List

def parse(inp: str) -> List[List]:
    """Function to parse"""
    return [list(i) for i in open(inp, 'r', encoding="utf-8").read().splitlines()]

def empties(inp: List[List]) -> tuple[List, List]:
    """Function to find empty rows/cols"""
    rows = sorted(list(set(index if '#' not in inp[index] else -2 for index in range(len(inp)))))[1:]
    cols = sorted(list(set(index if '#' not in list(zip(*inp))[index] else -2 for index in range(len(inp[0])))))[1:]
    return(rows, cols)

def vertices(inp: List[List]) -> List[tuple[int, int]]:
    """Function to find galaxy coords"""
    return [(row, col) for row, row_list in enumerate(inp) for col, element in enumerate(row_list) if element == '#']

def distance(gal1: tuple[int, int], gal2: tuple[int, int], expands: tuple[List, List]) -> int:
    """Function to return distance between two galaxies"""
    r_delta = abs(gal1[0] - gal2[0]) + sum(1 for expand in expands[0] if min(gal1[0], gal2[0]) < expand < max(gal1[0], gal2[0]))
    c_delta = abs(gal1[1] - gal2[1]) + sum(1 for expand in expands[1] if min(gal1[1], gal2[1]) < expand < max(gal1[1], gal2[1]))

    return r_delta + c_delta

def a(inp: str) -> int:
    """Solution to part A"""
    parsed = parse(inp)
    expands = empties(parsed)
    galaxies = vertices(parsed)

    return sum(distance(galaxies[i], galaxies[j], expands) for i in range(len(galaxies)) for j in range(i + 1, len(galaxies)) )

print(a("input.txt"))
