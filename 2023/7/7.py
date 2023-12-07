from functools import cmp_to_key
i = open('input.txt', 'r').read().splitlines()

hands = []

for line in i:
    hand, bid = line.split()
    hands.append((hand, int(bid)))

def ranker(card):
    freq = {}
    big = 0
    smoll = 10
    for char in card:
        freq[char] = freq.get(char, 0) + 1
        smoll = min(smoll, freq[char])
        big = max(big, freq[char])
    if big >= 4:
        return big + 2
    if big == 3:
        return 5 if len(freq.keys()) == 2 else 4
    if big == 2:
        return 3 if len(freq.keys()) == 3 else 2
    return 1

def compare(A, B):
    a = A[0]
    b = B[0]
    a_rank = ranker(a)
    b_rank = ranker(b)
    if a_rank > b_rank:
        return 1
    if a_rank < b_rank:
        return -1
    
    weight = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    for index in range(5):
        a_weight = weight[a[index]]
        b_weight = weight[b[index]]
        if a_weight > b_weight:
            return 1
        if a_weight < b_weight:
            return -1
    return 0
            

ranked = sorted(hands, key=cmp_to_key(compare))
print(sum((index+1)*hand[1] for index, hand in enumerate(ranked)))
