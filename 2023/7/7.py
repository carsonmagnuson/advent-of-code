from functools import cmp_to_key
import re
i = open('test.txt', 'r').read().splitlines()

hands = []
weight = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 1, 'Q': 12, 'K': 13, 'A': 14}

for line in i:
    hand, bid = line.split()
    hands.append((hand, int(bid)))

def ranker(card):
    freq, heavy = {}, 'J'
    for char in card:
        freq[char] = freq.get(char, 0) + 1

    heavy = max(freq.keys(), key=lambda x: weight[x])

    if freq.get('J') and freq['J'] != 5:
        jokes = freq['J']
        del freq['J']
        freq[heavy if len(freq.keys()) == 5 else max(freq.keys(), key=lambda x: freq[x])] += jokes

    big, variance = max(freq.values()), len(freq.keys()) 

    if big >= 4: return big + 2
    if big == 3: return 5 if variance == 2 else 4
    if big == 2: return 3 if variance == 3 else 2
    return 1

def compare(A, B):
    diff = ranker(A[0]) - ranker(B[0])
    return (diff) / abs(diff) if diff != 0 else weigh_deez(A[0], B[0])

def weigh_deez(a, b):
    comparisons = ''.join(str(weight[card_a] - weight[card_b]) for card_a, card_b in zip(a,b))
    print(comparisons)
    kicker = re.search(r'-?[1-9]\b', comparisons)
    print(kicker)
    for index in range(5):
        diff = weight[a[index]] - weight[b[index]]
        if diff != 0: return (diff) / abs(diff)
            

ranked = sorted(hands, key=cmp_to_key(compare))
print(sum((index+1)*hand[1] for index, hand in enumerate(ranked)))
