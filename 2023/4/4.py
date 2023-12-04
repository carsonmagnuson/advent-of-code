from math import pow
input = open('input.txt', 'r').read().splitlines()

def part_a(lines):
    scores = []
    for line in lines:
        numbers = line[line.find(':') + 1:]
        win, mine = numbers.split('|')
        win = set(list(map(int, win.split())))
        mine = list(map(int, mine.split())) 
        score = 0
        for num in mine:
            if num in win:
                score += 1
        scores.append(score)

    print(sum(map(lambda x: 1*pow(2,x-1) if x else 0, scores)))

    total = 0
    for x in range(len(scores)):
        total += 1 + recur(x, scores)
    print(total)

def recur(index, scores):
    cumulative = 0
    for x in range(1, scores[index]+1):
        cumulative += recur(index+x, scores)
    return scores[index] + cumulative 


part_a(input)
