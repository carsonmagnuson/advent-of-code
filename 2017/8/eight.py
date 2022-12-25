from collections import defaultdict

i_n = list(l.split(' ') for l in open('2017/8/input.txt').read().splitlines())
operations = {'<' : lambda x, y : x < y, '>' : lambda x, y : x > y, '<=' : lambda x, y : x <= y, '>=' : lambda x, y : x >= y,'==' : lambda x, y : x == y, '!=' : lambda x, y : x != y}
def part_one(i_n):
    registers = defaultdict(lambda x = 0: x)
    for input in i_n:
        if operations[input[5]](registers[input[4]], int(input[6])):
            registers[input[0]] = registers[input[0]] + int(input[2]) if input[1] == 'inc' else registers[input[0]] - int(input[2])
            
    return max(registers.values())

def part_two(input):
    big = 0
    registers = defaultdict(lambda x = 0: x)
    for input in i_n:
        if operations[input[5]](registers[input[4]], int(input[6])):
            registers[input[0]] = registers[input[0]] + int(input[2]) if input[1] == 'inc' else registers[input[0]] - int(input[2])
            big = max(big, registers[input[0]])
            
    return big


print(part_one(i_n))
print(part_two(i_n))

