i_n = list(l.split(' ') for l in open('2017/4/input.txt').read().splitlines())




def part_one(i_n):
    return sum(len(l) == len(set(l)) for l in i_n)
    # total = 0
    # for l in i_n: total += 1 if len(l) == len(set(l)) else 0
    # return total

def part_two(i_n):
    total = 0
    for l in i_n:
        sorted_set = set()
        valid = True
        for w in l:
            word = ''.join(sorted(list(w)))
            if word not in sorted_set:
                sorted_set.add(word)
            else:
                valid = False
                break
        if valid:
            total += 1
    return total

print(part_one(i_n))
print(part_two(i_n))

