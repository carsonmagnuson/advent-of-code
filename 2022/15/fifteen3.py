# decided to open a new file, because I'm about to scramble this up. Okay so it's been about 2 hours since that last comment, and I've realized I think I need to rewrite this code from scratch for the second part, because it just doesn't work like this.

from re import findall
from collections import defaultdict

print('Prime salutations, goodman. Code registering now.')

i_n = list(list(map(int, findall(r"-?\d+", l))) for l in open('2022/15/input.txt').read().splitlines())
useful = []
space = []
lower_bound = 0
upper_bound = 4000000

for coords in i_n:
    x = coords[0]
    y = coords[1]
    # we will always need the delta for checks
    delta = abs(coords[0] - coords[2]) + abs(coords[1] - coords[3])
    # useful.append(((x,y), delta))
    # we need to check if the sensor is inside the space first, if so then pre-render it.
    inside_y = y <= upper_bound and y >= lower_bound
    inside_x = x <= upper_bound and x >= lower_bound
    if inside_x and inside_y:
        useful.append(((x, y), delta))
    ## y value checking
    # elif y < lower_bound: # checking if lower than lower boundary
    #     if y + delta >= lower_bound: # checking if delta crosses boundary
    #         useful.append(((x, y), delta)) ## storing coords and delta info for later
    # elif y > upper_bound : # checking if higher than higher boundary
    #     if y - delta <= upper_bound: # checking if delta crosses boundary
    #         useful.append(((x, y), delta)) # ..
    # ## x value checking
    # elif x < lower_bound: # checking if lower than lower boundary
    #     if x + delta >= lower_bound: # checking if delta crosses boundary
    #         useful.append(((x, y), delta)) ## storing coords and delta for later
    # elif x > upper_bound : # checking if higher than higher boundary
    #     if x - delta <= upper_bound: # checking if delta crosses boundary
    #         useful.append(((x, y), delta)) # ..

# print(useful)
useful = sorted(useful, key=lambda x: x[0][0])
print(useful)

def merge_interval(coverage, coords, old):
    new = [coords[0] - coverage, coords[0] + coverage]
    if old[1] + 1 >= new[0]: return [old[0] if old[0] < new[0] else new[0], new[1] if new[1] > old[1] else old[1]]
    else: return old

def check_lines(useful):
    for space_y_line in range(upper_bound + 1):
        interval = [0,0]
        for coords, delta in useful:
            difference = abs(coords[1] - space_y_line)
            if difference <= delta:
                interval = merge_interval(delta-difference, coords, interval)
        # print(interval)
        if interval[1] <= upper_bound:
            print(f"We're on x: {interval[1] + 1} and y: {space_y_line} ")
            print(f"Answer =: {4000000*(interval[1] + 1) + space_y_line} ")

            return
            
## okay okay so I'm merging intervals now, and I just realized, I may get a problem say if one interval is skipped in the list, but the next interval will fill that space.

check_lines(useful)

