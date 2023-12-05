i = open('input.txt', 'r').read().split('\n\n')

i = [line.strip() for line in i]

seeds = list(map(int, i[0][i[0].find(':')+1:].split()))
seedsv2 = list((seeds[a], seeds[a+1]) for a in range(0, len(seeds), 2)) 

def wormhole(grav_map, seed):
    grav_map = grav_map.split()[2:]
    for y, x, gap in [list(map(int, [grav_map[x], grav_map[x+1], grav_map[x+2]])) for x in range(0, len(grav_map), 3)]:
        if seed >= x and seed <= x + gap-1:
            delta = seed - x
            return y + delta
    return seed

        
seed_bank = []
dominant = float('inf')

for seed in seeds:
    gmo = seed
    for grav_map in i[1:]:
        gmo = wormhole(grav_map, gmo)
    seed_bank.append(gmo)

print('Spinning up seed contest part two...')
for start, delta in seedsv2:
    for seed in range(start, start+delta-1):
        if seed%100000000 == 0:
            print(f'seeding number {seed}')
        for grav_map in i[1:]:
            seed = wormhole(grav_map, seed)
        dominant = min(seed, dominant)

#test = 82
#for grav_map in i[1:]:
    #test = wormhole(grav_map, test)
#print(test)

print(dominant)
# print(min(seed_bank))
