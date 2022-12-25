i_n = open('input.txt').read().splitlines()
from re import findall

def part_one(i_n):
    return sum(max(chars)-min(chars) for chars in list(list(map(int, findall(r"\d+", l))) for l in i_n))

def part_two(i_n):
    t = 0
    for l in i_n:
        chars = list(map(int, findall(r"\d+", l)))
        for char1 in range(len(chars)):
            for char2 in range(len(chars)):
                if chars[char1] % chars[char2] == 0 and char1 != char2:
                    t += max(chars[char1], chars[char2]) / min(chars[char1], chars[char2])


    return t

print(part_one(i_n))
print(part_two(i_n))



