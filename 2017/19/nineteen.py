i_n = list(list(i) for i in open('input.txt').read().splitlines())

motions = { 'r': (lambda x, y: (x + 1, y)), 'l': (lambda x, y: (x - 1, y)), 'u': (lambda x, y:(x, y - 1)), 'd': (lambda x, y: (x, y + 1)) }
def part_a(input):
    def check(pos, input): 
        return True if pos[0] > -1 and pos[1] > -1 and pos[0] < len(input[0]) and pos[1] < len(input) and input[pos[1]][pos[0]] != ' ' else False

    def hasNext(curr, last, input):
        current = input[curr[1]][curr[0]]
        if current != '+':
            return (curr[0] + (curr[0] - last[0]), curr[1] + (curr[1] - last[1])) if input[curr[1] + (curr[1] - last[1])][(curr[0] + (curr[0] - last[0]))] != ' ' else None
        else:
            for m in motions.keys():
                x, y = curr
                transformed = motions[m](x, y)
                if check(transformed, input) and transformed != last:
                    return transformed

    message = ''
    last = (0,-1)
    curr = (0,0)
    for index in range(len(input[0])):
        if input[0][index] != ' ':
            curr = (index, curr[1])
            last = (index, last[1])
    print(curr)
    total = 0
    while curr[1] < len(input) and curr[0] < len(input[0]) and curr[1] > -1 and curr[0] > -1:
        # print(f'curr = {curr}, last = {last}')
        message = ''.join([message, input[curr[1]][curr[0]]]) if input[curr[1]][curr[0]].isupper() else message
        next = hasNext(curr, last, input)
        if next:
            last = curr
            curr = next
            total += 1
        else:
            print(total + 1)
            break
    return message


message = part_a(i_n)
print(message)
