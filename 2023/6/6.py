import re
i = open('input.txt','r').read().splitlines()

def part_a(i):
    times = list(map(int, i[0][i[0].find(':')+1:].split()))
    records = list(map(int, i[1][i[1].find(':')+1:].split()))
    total = 1

    for index, time in enumerate(times):
        winners = 0
        for hold in range(time):
            distance = hold*(time-hold)
            if distance > records[index]:
                winners += 1
        total *= winners

    print(total)

def part_b(i):
    total = 0
    time = int(''.join(re.findall(r'\b\d+\b', i[0])))
    record = int(''.join(re.findall(r'\b\d+\b', i[1])))
    for hold in range(time):
        distance = hold*(time-hold)
        if distance > record:
            total += 1
    print(total)
    

    
    

part_b(i)
