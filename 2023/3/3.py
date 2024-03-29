input = open('input3.txt', 'r').read().splitlines()

def findnum(coords, lines):
    row, end = coords
    row, beg = coords 
    while end < len(lines[0]) and lines[row][end].isdigit():
        end += 1
    while beg >= 0 and lines[row][beg].isdigit():
        beg -= 1

    return str(row) + " " + str(beg+1) + " " + str(end)

def part_a(lines):
    symbols = []
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char != '.' and not char.isdigit():
                symbols.append((row, col))

    nums = set()
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
    for s_row, s_col in symbols:
        for x, y in moves:
            if lines[s_row + x][s_col + y].isdigit():
                num = findnum((s_row + x, s_col + y), lines)
                nums.add(num)

    numbers = [int(lines[int(row)][int(beg):int(end)]) for row, beg, end in (num.split() for num in list(nums))]

    print(sum(numbers))

def part_b(lines):
    symbols = []
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == '*':
                symbols.append((row, col))

    gearsets = []
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
    for s_row, s_col in symbols:
        gear = set()
        for x, y in moves:
            if lines[s_row + x][s_col + y].isdigit():
                num = findnum((s_row + x, s_col + y), lines)
                row, beg, end = num.split()
                #print(int(lines[int(row)][int(beg):int(end)]))
                gear.add(num)
                #print(gear)
        if len(gear) == 2:
            gearsets.append(list(gear))
        # print(gearsets)
                

    summation = 0

    for gear in gearsets:
        ratio = []
        for num in gear:
            row, beg, end = num.split()
            ratio.append(int(lines[int(row)][int(beg):int(end)]))
        summation += ratio[0] * ratio[1]
        

    print(summation)





#part_a(input)
part_b(input)
