from typing import List


def parse(inp: str) -> List:
    """Function to parse input"""
    return [list(l) for l in open(inp, 'r', encoding='utf-8').read().splitlines()]

energized = set()
visited = set()
def trace(cave: List, curr: tuple, move: tuple):
    """Function to trace"""
    r, c = curr
    moves = {(-1, 0): 'up', (1, 0): 'down', (0, -1): 'left', (0, 1): 'right'}
    while True:
        # draw(cave)
        # print(r, c, moves[move])
        # print()
        if r > -1 and c > -1:
            energized.add((r, c))
            if (r, c, move) in visited:
                return
            visited.add((r, c, move))
        r, c  = r + move[0], c + move[1]
        if r > len(cave) - 1 or r < 0 or c > len(cave[0]) - 1 or c < 0:
            return
        if cave[r][c] == '|':
            if move[1] != 0: # check if we're coming at the splitter directly
                trace(cave, (r, c), (-1, 0))
                trace(cave, (r, c), (1, 0))
                return
        elif cave[r][c] == '-':
            if move[0] != 0:
                trace(cave, (r, c), (0, -1))
                trace(cave, (r, c), (0, 1))
                return
        elif cave[r][c] == '/':
            trace(cave, (r, c), (move[1] * -1, move[0] * -1))
            return
        elif cave[r][c] == '\\':
            trace(cave, (r, c), (move[1], move[0]))
            return

def draw(parsed):
    for row in range(len(parsed)):
        for col in range(len(parsed)):
            print('#' if (row, col) in energized else '.', end='')
        print('')

trace(parse('1'), (0, -1), (0, 1))
print(len(energized))

