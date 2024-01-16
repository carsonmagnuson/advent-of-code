"""
This module contains functions to process a grid representing galaxies and calculate distances between galaxies.

Functions:
- parse(inp: str) -> List[list]: Parse the input file and return a 2D list representing the grid of galaxies.
- empties(inp: List[list]) -> tuple[list, list]: Identify empty rows and columns in the grid.
- vertices(inp: List[list]) -> list[tuple[int, int]]: Find the coordinates of galaxies in the grid.
- distance(gal1: tuple[int, int], gal2: tuple[int, int], expands: tuple[List, list], modifier: int) -> int: Calculate the distance between two galaxies.
- a(inp: str) -> int: Solution to part a, calculating the total distance between pairs of galaxies.
- b(inp: str, modifier: int) -> int: Solution to part b, calculating the total distance between pairs of galaxies with a modifier.

Usage:
- Run `a("input.txt")` to get the solution for part a.
- Run `b("input.txt", 1000000)` to get the solution for part b with a modifier.
"""

from typing import List


def parse(inp: str) -> List[List]:
    """function to parse"""
    return [list(i) for i in open(inp, "r", encoding="utf-8").read().splitlines()]


def empties(inp: List[List]) -> tuple[List, List]:
    """function to find empty rows/cols"""
    rows = sorted(
        list(set(index if "#" not in inp[index] else -1 for index in range(len(inp))))
    )[1:]
    cols = sorted(
        list(
            set(
                index if "#" not in list(zip(*inp))[index] else -1
                for index in range(len(inp[0]))
            )
        )
    )[1:]
    return (rows, cols)


def vertices(inp: List[list]) -> list[tuple[int, int]]:
    """function to find galaxy coords"""
    return [
        (row, col)
        for row, row_list in enumerate(inp)
        for col, element in enumerate(row_list)
        if element == "#"
    ]


def distance(
    gal1: tuple[int, int],
    gal2: tuple[int, int],
    expands: tuple[List, list],
    modifier: int,
) -> int:
    """function to return distance between two galaxies"""
    r_delta = abs(gal1[0] - gal2[0]) + sum(
        modifier
        for expand in expands[0]
        if min(gal1[0], gal2[0]) < expand < max(gal1[0], gal2[0])
    )
    c_delta = abs(gal1[1] - gal2[1]) + sum(
        modifier
        for expand in expands[1]
        if min(gal1[1], gal2[1]) < expand < max(gal1[1], gal2[1])
    )

    return r_delta + c_delta


def a(inp: str) -> int:
    """solution to part a"""
    parsed = parse(inp)
    expands = empties(parsed)
    galaxies = vertices(parsed)

    return sum(
        distance(galaxies[i], galaxies[j], expands, 1)
        for i in range(len(galaxies))
        for j in range(i + 1, len(galaxies))
    )


def b(inp: str, modifier: int) -> int:
    """solution to part b"""
    parsed = parse(inp)
    expands = empties(parsed)
    galaxies = vertices(parsed)

    return sum(
        distance(galaxies[i], galaxies[j], expands, modifier - 1)
        for i in range(len(galaxies))
        for j in range(i + 1, len(galaxies))
    )


print(a("input.txt"))
print(b("input.txt", 1000000))
