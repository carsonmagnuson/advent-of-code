from typing import List


def parse(inp: str) -> List:
    """Function to parse input"""
    return open(inp, 'r', encoding= 'utf-8').read().rstrip().split(',')

def hashish(inp: 'str') -> int:
    """Function hash a string"""
    value = 0
    for char in inp:
        value += ord(char)
        value *= 17
        value %= 256
    return value

def interpret(opcode: 'str') -> List:
    """Function to intepret lense code"""
    lense = opcode.split('=') if '=' in opcode else [opcode[:-1]]
    return lense

def install(opcodes: List) -> tuple:
    """Function to simulate lense installations"""
    boxes = {}
    ordering = {}
    for opcode in opcodes:
        lens = interpret(opcode)
        box = hashish(lens[0])
        if len(lens) == 1 and box not in boxes:
            continue
        if box not in boxes:
            boxes[box] = {}
            ordering[box] = []
        if len(lens) == 2:
            if lens[0] not in ordering[box]:
                ordering[box].append(lens[0])
            boxes[box][lens[0]] = lens[1]
        else:
            if lens[0] in boxes[box]:
                del boxes[box][lens[0]]
                ordering[box].remove(lens[0])

    return (boxes, ordering)

def focus(info: tuple) -> int:
    """Function to determine focusing power"""
    boxes, ordering = info
    total = 0
    for box in ordering.keys():
        for slot, lens in enumerate(ordering[box]):
            total += (int(box) + 1) * (int(slot) + 1) * int(boxes[box][lens])
    return total


def a(inp: str) -> int:
    """Solution for pt a"""
    parsed = parse(inp)
    return sum(hashish(step) for step in parsed)

def b(inp: str) -> int:
    """Solution for pt b"""
    parsed = parse(inp)
    return focus(install(parsed))

print(a('1'))

print(b('1'))
