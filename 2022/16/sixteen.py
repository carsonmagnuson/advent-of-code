from re import findall

i_n = list(list(map(int if not TypeError else str, findall(r"-?\d+|[A-Z]{2}", l))) for l in open('2022/16/input.txt').read().splitlines())

print(i_n)