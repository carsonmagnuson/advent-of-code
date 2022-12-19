# decided to open a new file, because I'm about to scramble this up. Okay so it's been about 2 hours since that last comment, and I've realized I think I need to rewrite this code from scratch for the second part, because it just doesn't work like this. IT still doesn't work, so we're trying something else in a new file.

from re import findall
from collections import defaultdict

print('Prime salutations, goodman. Code registering now.')

i_n = list(list(map(int, findall(r"-?\d+", l))) for l in open('2022/15/input.txt').read().splitlines())
useful = []
space = []
lower_bound = 0
upper_bound = 4000000

def check(space_x, space_y, coords, delta):
    x,y = coords
    difference = abs(space_y - y) + abs(space_x - x)
    if difference <= delta:
        return True
    else:
        return False


for coords in i_n:
    x = coords[0]
    y = coords[1]
    # we will always need the delta for checks
    delta = abs(coords[0] - coords[2]) + abs(coords[1] - coords[3])
    ## we need to check if the sensor is inside the space first, if so then pre-render it.
    inside_y = y <= upper_bound and y >= lower_bound
    inside_x = x <= upper_bound and x >= lower_bound
    if inside_x and inside_y:
        useful.append(((x, y), delta))
    ## y value checking
    elif y < lower_bound: # checking if lower than lower boundary
        if y + delta >= lower_bound: # checking if delta crosses boundary
            useful.append(((x, y), delta)) ## storing coords and delta info for later
    elif y > upper_bound : # checking if higher than higher boundary
        if y - delta <= upper_bound: # checking if delta crosses boundary
            useful.append(((x, y), delta)) # ..
    ## x value checking
    elif x < lower_bound: # checking if lower than lower boundary
        if x + delta >= lower_bound: # checking if delta crosses boundary
            useful.append(((x, y), delta)) ## storing coords and delta for later
    elif x > upper_bound : # checking if higher than higher boundary
        if x - delta <= upper_bound: # checking if delta crosses boundary
            useful.append(((x, y), delta)) # ..
    
print('Useful coordinates found, moving to render check.')
## Okay now we have a list of coords and their respective deltas to go render.
# I suppose we do two renders depending on–actually wait. I have a cool idea.

def renderer(useful):
    for space_y in range(upper_bound + 1):
        for space_x in range(upper_bound + 1):
            if space_x % 1000000 == 0:
                print(f"We're on coords {space_x}, {space_y}")
            covered = False
            for coords, delta in useful:
                if check(space_x, space_y, coords, delta):
                    covered = True
                    break
            if not covered:
                print(f'x val = {space_x}, y val = {space_y}')
                return

    return
# renderer(useful)
print(useful)



for space_y in range(upper_bound + 1):
    print(f"We're on y coords {space_y}")
    for space_x in range(upper_bound + 1):
        checker = 0

