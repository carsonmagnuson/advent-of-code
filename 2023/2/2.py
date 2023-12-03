from math import prod
input = open('input.txt', 'r').read().splitlines()

# idlists = [((types for types in round.strip().split(',')) for round in game[game.find(':') + 1:].split(';')) for index, game in enumerate(lines)]

def part_a(lines):
    powersets = []
    idlist = []
    for index, line in enumerate(lines):
        maxmin = {'r':0, 'g':0, 'b':0}
        badgame = False
        game = line[line.find(':') + 1:].split(';')
        for round in game:
            types = round.strip().split(',')
            
            vals = {'r':0, 'g':0, 'b':0}
            for marb in types:
                marb = marb.strip().split(' ')
                vals[marb[1][0]] = int(marb[0])

            for color in maxmin.keys():
                maxmin[color] = max(maxmin[color], vals[color])

            if vals['r'] <= 12 and vals['g'] <= 13 and vals['b'] <= 14:
                continue
            else:
                badgame = True
        if not badgame:
            idlist.append(index + 1)
            badgame = False
        
        
        powersets.append(prod(maxmin.values()))


    print(sum(idlist))
    print(sum(powersets)) 

part_a(input)
