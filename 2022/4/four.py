lines = open('2022/4/input.txt', 'r').read().splitlines()
count = 0
count2 = 0
for line in lines:
    pairs = line.split(',')
    l = list(map(int, pairs[0].split('-')))
    r = list(map(int, pairs[1].split('-')))
    for x in range(0, 100, 10):
        f = '.'
        print(f'{int(str(x)[0]) if int(str(x)[0]) >= int(str(l[0])[0]) and int(str(x)[0]) <= int(str(l[1])[0]) else f}', end = ' ') ## issue: denominations under 10, their first digit is going to be 1-9
    print()
    for x in range(0, 100, 10):
        f = '.'
        print(f'{int(str(x)[0]) if int(str(x)[0]) >= int(str(r[0])[0]) and int(str(x)[0]) <= int(str(r[1])[0]) else f}', end = ' ')
    print()
    print(f'l elf: {l} and r left: {r}')
    if l[0] <= r[0] and l[1] >= r[1]:
        count += 1
        print('yes')
    elif r[0] <= l[0] and r[1] >= l[1]:
        count += 1
        print('yes')
    else:
        print('no')
    
    contained = set()
    for x in range(l[0], l[1]+1):
        contained.add(x)
    for x in range(r[0], r[1]+1):
        if x in contained:
            count2 += 1
            break
print(count)
print(count2)
