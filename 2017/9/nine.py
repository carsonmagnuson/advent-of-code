i_n = open('2017/9/input.txt').read()

def both_parts(line):
    score = 0
    current_value = 1
    trash = False
    index = 0
    non_trash_count = 0
    while index < len(line) - 1:
        if not trash:
            if line[index] == '{':
                score += current_value
                current_value += 1
            elif line[index] == '}': current_value -= 1
            elif line[index] == '<': trash = True
            elif line[index] == '!': index += 1
        elif line[index] == '>': trash = False
        elif line[index] == '!':
            index += 2
            continue
        else: non_trash_count += 1
        index += 1
    return (score, non_trash_count)

ans = both_parts(i_n)
print(ans[0])
print(ans[1])