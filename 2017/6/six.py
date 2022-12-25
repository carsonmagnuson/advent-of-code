import re
i_n = list(map(int, re.split('\s+', open('2017/6/input.txt').read())))
print(i_n)

def part_one(input):
    states = set()
    currState = ''.join(list(map(str, input)))
    cycles = 0
    while currState not in states:
        states.add(currState)
        cycles += 1
        big = max(input)
        stack = -1
        count = 0
        while stack < big:
            if stack > -1:
                input[count%len(input)] += 1
                stack += 1
            if input[count%len(input)] == big and stack < 0:
                input[count%len(input)] = 0
                stack += 1
            count += 1
        currState = ''.join(list(map(str, input)))
    return cycles

def part_two(input):
    states = {}
    currState = ''.join(list(map(str, input)))
    cycles = 0
    while True:
        states[currState] = cycles
        cycles += 1
        big = max(input)
        stack = -1
        count = 0
        

        while stack < big:
            if stack > -1:
                input[count%len(input)] += 1
                stack += 1
            if input[count%len(input)] == big and stack < 0:
                input[count%len(input)] = 0
                stack += 1
            count += 1

        currState = ''.join(list(map(str, input)))
        if states.get(currState) != None:
            return cycles - states.get(currState)
print(part_one(i_n))
print(part_two(i_n))
