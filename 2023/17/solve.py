from typing import Deque, List

@dataclass
class 

def parse(inp: str) -> List:
    """Function to parse input"""
    return [list(l) for l in open(inp, 'r', encoding="utf-8").read().splitlines()]

def loss(inp: List, initial: tuple, dest: tuple) -> int:
    """Function to determine least heat loss possible"""
    visited = {}
    q = Deque([(initial, 0)])

    
