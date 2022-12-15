
## okay this sprite pixel jawn (pt 2) is annoying so many moving parts. From what I can tell
# it's all about telling if the x register +- 1 == the cycle, and if it does,
# you get a light pixel. Otherwise you get a dark pixel. So lets try to do that.
# okey we done. ez pz. 

i, c, x = open('2022/10/input.txt').read().splitlines(), 0, 1

for l in i:
    for j in range(1 if l == 'noop' else 2):
        print('#' if abs(x - c) < 2 else ' ', end='')
        c += 1
        if c > 39:
            print()
            c = 0
        # if (c + 20) % 40 == 0 and not c > 220:
            # print(f'x: {x} and c: {c} and strength is: {c*x}')
            
            # count += c * x
    x += int(l.split()[1] if l != 'noop' else 0)



