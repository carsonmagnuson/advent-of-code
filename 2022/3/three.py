## pt 1 find sum of the priorities of each one-time-occurring letter that appears in both halves of the string.
## the first thing to do is come up with and algorithm that allows us to check the first half of a string against the second half looking for the duplicate

input = open('2022/3/input.txt', 'r').read().splitlines() 
simul = []
for line in input:
    check = set()
    for index in range(0, len(line)//2):
        check.add(line[index])
    for index in range(len(line)//2, len(line)):
        if line[index] in check:
            simul.append(line[index])
            break
total = 0
for char in simul:
    total += ord(char) - 38 if char.isupper() else ord(char) - 96
print(total)
badge = []
for line in range(0, len(input), 3):
    round1 = set()
    round2 = set()
    for index in range(0, len(input[line])):
        round1.add(input[line][index])
    line2 = line + 1
    for index in range(0, len(input[line2])):
        curr = input[line2][index]
        if curr in round1:
            round2.add(input[line2][index])
    line3 = line2 + 1
    for index in range(0, len(input[line3])):
        curr = input[line3][index]
        if curr in round2:
            badge.append(input[line3][index])
            break
total = 0
for char in badge:
    total += ord(char) - 38 if char.isupper() else ord(char) - 96    
print(total)
    



# print(input)