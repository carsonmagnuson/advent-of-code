i_n = open('input.txt', 'r').read()

def part_one(input):
    s = 0
    for i in range(len(i_n)):
        if i_n[i] == i_n[(i + 1) % len(i_n)]:
            s += int(i_n[i])
    return s

def part_two(input):
    s = 0
    for i in range(len(i_n)):
        if i_n[i] == i_n[(i + (len(i_n)//2)) % len(i_n)]:
            s += int(i_n[i])
    return s


print(f'pt 1: {part_one(i_n)}, pt 2: {part_two(i_n)}.')


