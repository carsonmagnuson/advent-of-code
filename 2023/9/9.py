def doparse(input):
    input = [list(map(int, l.split())) for l in open(input, 'r').read().splitlines()]
    return input

def b(line):
    bex = 0
    for el in line[::-1]:
        bex = el[0] - bex
    return bex
        
        

def a(input):
    ex = []
    bex = []
    for ser in input:
        line = [ser]
        while sum(line[-1]):
            curr = []
            for index in range(len(line[-1])-1):
                curr.append(line[-1][index + 1] - line[-1][index])
            line.append(curr)

        ex.append(sum(line[i][-1] for i in range(len(line))))
        bex.append(b(line))

    print(sum(bex))
    return sum(ex)








input = doparse('input.txt')
print(a(input))
