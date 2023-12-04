from math import pow
input = open('test.txt', 'r').read().splitlines()

def sol(lines):
    scores = [len(set(map(int, win.split())).intersection(list(map(int, mine.split())))) for win, mine in (numbers.split('|') for numbers in (line[line.find(':')+1:] for line in lines))]

    print('part A:')
    print(sum(map(lambda x: 1*pow(2,x-1) if x else 0, scores)))

    print('part B:')
    print(sum(1 + recur(x, scores) for x in range(len(scores))))


def recur(index, scores):
    return scores[index] + sum(recur(index+x, scores) for x in range(1, scores[index]+1))


sol(input)
