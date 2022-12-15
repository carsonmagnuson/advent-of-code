# def foo(p, o) -> int:
#     if ord(o) == ord(p) + 23: ## A(rock) = 65, X(rock) = 88 -- draw
#         return 3
#     elif ord(o) == ord(p) + 22: ## B(paper) = 66, X(rock) = 88 -- loss
#         return 0
#     elif ord(o) == ord(p) + 24: ## A(rock) = 65, Y(paper) = 87 -- win
#         return 6
#     elif ord(o) == ord(p) + 21: ## C(scissors) = 67, X(rock) = 88 -- Win
#         return 6
#     elif ord(o) == ord(p) + 25: ## A = 65, Z = 90
#         return 0

# total = 0
# for x in open('2022/2/input.txt','r').readlines():
#     x = x.strip().split()
#     if x[1] is 'X':
#         total += 1
#     elif x[1] is 'Y':
#         total += 2
#     elif x[1] is 'Z':
#         total += 3
#     print(x[0], x[1])
#     total += foo(x[0], x[1])

# print(total)

total = 0
for x in open('2022/2/input.txt','r').readlines():
    x = x.strip().split()
    ##lose
    if x[1] == 'X':
        plus = ord(x[0]) - 65
        if plus > 0:
            total += plus
        else:
            total += 3
        print(f'plus = {plus}, opponent uses: {x[0]}, and your value is {x[1]}')
    ##draw
    if x[1] == 'Y':
        total += ord(x[0]) - 64 + 3
    ##win
    if x[1] == 'Z':
        plus = ord(x[0]) - 63
        if plus > 3:
            total += 1 + 6
        else:
            total += plus + 6
        print(f'plus = {plus}, opponent uses: {x[0]}, and your value is {x[1]}')

print(total)


