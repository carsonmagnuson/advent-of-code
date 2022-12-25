from copy import deepcopy
i_n = list(map(int, open('2017/5/input.txt').read().splitlines()))


def part_one(input):
    index, count = 0, 0
    while index < len(input) and index > -1:
        count += 1
        temp = input[index]
        input[index] += 1
        index += temp
    return count

def part_two(input):
    index, count = 0, 0
    while index < len(input) and index > -1:
        count += 1
        temp = input[index]
        input[index] = input[index] - 1 if input[index] >= 3 else input[index] + 1
        index += temp
    return count

print(part_one(deepcopy(i_n)))
print(part_two(deepcopy(i_n)))