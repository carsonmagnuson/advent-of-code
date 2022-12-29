from dataclasses import dataclass
from typing import List
i_n = list(l.split(' ') for l in open('2017/7/input.txt').read().splitlines())

##I need to find all the lists that have stuff on top of them, then find one that isn't in a top-sublist of any other list
@dataclass
class Program:
    name: str
    size: int
    children: List[str] or bool


def part_one(input):
    potential_root_names, listed_non_root_names = set(), set()
    for l in input:
        if len(l) > 2:
            potential_root_names.add(l[0])
            for index in range(3, len(l)): listed_non_root_names.add(l[index][:-1] if index != len(l) - 1 else l[index])
    for item in potential_root_names: 
        if item not in listed_non_root_names: return item

def part_two(input, start):
    # okay so for this problem I think we have to create a data structure and then traverse it recursively to check sizes. I think we use a hashmap of names pointing to specific data classes that then contain a list of strings of names that they potentially are balancing.
    programs = {}
    for l in input:
        children = []
        if len(l) > 2:
            for index in range(3, len(l)): children.append(l[index][:-1] if index != len(l) - 1 else l[index])
        current = Program(l[0], int(l[1][1:-1]), children if len(children) > 0 else False)
        programs[l[0]] = current
    ## data structure is created. Now we traverse it recursively
    fixed_balance = recur(start, programs)
    return fixed_balance[0]


def recur(start, programs):
    if programs[start].children:
        totals = []
        for child in programs[start].children:
            go_deeper = recur(child, programs)
            if go_deeper[1]: return(go_deeper[0], True)
            else: totals.append(go_deeper[0])
        sum_of_totals = sum(total for total in totals)
        if sum_of_totals/len(totals) == totals[0]: return (programs[start].size + sum_of_totals, False)
        else:
            total_counts = {}
            for total in totals: total_counts[total] = total_counts.get(total, 0) + 1
            majority, unique = max(total_counts, key=total_counts.get), min(total_counts, key=total_counts.get)

            unique_name_index = ''
            for index, number in enumerate(totals): 
                if number == unique: unique_name_index = index

            offending_program = programs[start].children[unique_name_index]
            transform = majority - unique

            return ((programs[offending_program].size + transform), True)
    else: return (programs[start].size, False)

print(part_one(i_n))
print(part_two(i_n, part_one(i_n)))