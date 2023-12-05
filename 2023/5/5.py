i = open('test.txt', 'r').read().split('\n\n')

i = [line.strip() for line in i]

seeds = list(map(int, i[0][i[0].find(':')+1:].split()))

def wormhole(grav_map, seed):
    grav_map = grav_map.split()[2:]
    for y, x, gap in [list(map(int, [grav_map[x], grav_map[x+1], grav_map[x+2]])) for x in range(0, len(grav_map), 3)]:
        if seed >= x and seed <= x + gap-1:
            delta = seed - x
            return y + delta
    return seed

        
seed_bank = []

for seed in seeds:
    gmo = seed
    for grav_map in i[1:]:
        gmo = wormhole(grav_map, gmo)
    seed_bank.append(gmo)

print(min(seed_bank))
