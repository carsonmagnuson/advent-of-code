
## there are three rules:
# one, if both values are ints, the left should contain lower one, if right contains lower then invalid, if same then continue
# two, if both are lists (and the first rule doesn't apply at any point) the left list should run out first, if right runs out first, invalid, else if same length then continue
# three, if one is list and one is int, make int a list and do compare

import json
import copy
iN = open('2022/13/input.txt').read().splitlines()
comps, crutch_list = [], []


# for index in range(0, len(iN), 3):
#     left = json.loads(iN[index + 1])
#     right = json.loads(iN[index])
#     comps.append((right, left))

for index in range(0, len(iN), 3):
    crutch_list.extend((json.loads(iN[index + 1]), json.loads(iN[index])))



def recur(left, right):
    c = 0
    while c < len(left) and c < len(right):
        if type(left[c]) == type(right[c]):
            if type(left[c]) == int:
                if left[c] > right[c]:
                    return False
                elif left[c] == right[c]:
                    c += 1
                    continue
                else:
                    return True
            else:
                valid = recur(left[c], right[c])
                if valid != None:
                    return valid
                else:
                    c += 1
                    continue
        else:
            left[c] = [left[c]] if type(left[c]) == int else left[c]
            right[c] = [right[c]] if type(right[c]) == int else right[c]
            valid = recur(left[c], right[c])
            if valid != None:
                return valid
            else:
                c += 1
                continue
    if c == len(left) and c == len(right):
        return None
    return False if c < len(left) else True

for i in range(len(crutch_list)):
    for j in range(len(crutch_list) - 1):
        valid = recur(copy.deepcopy(crutch_list[j]), copy.deepcopy(crutch_list[j + 1]))
        if not valid:
            temp = crutch_list[j]
            crutch_list[j] = crutch_list[j + 1]
            crutch_list[j + 1] = temp
        
# def merge(arr, start, end):

#     if end - start < 2:
#         return
    
#     newArr = []

#     mid = start + ((end - start) // 2)

#     merge(arr, start, mid)
#     merge(arr, mid + 1, end)

#     l, r = 0, mid
#     while l < mid or r < end + 1:
#         if not (l < mid):
#             newArr.append(arr[r])
#             r += 1
#         elif not (r < end):
#             newArr.append(arr[l])
#             l += 1
#         elif recur([copy.deepcopy(arr[l])], [copy.deepcopy(arr[r])]):
#             newArr.append(arr[l])
#             l += 1
#         else:
#             newArr.append(arr[r])
#             r += 1
    
#     for x in range(start, end + 1):
#         arr[x] = newArr[x - start]

#     return arr


# crutch_list = merge(crutch_list, 0, len(crutch_list) - 1)
# print(crutch_list)

total = 1
for crutch_index in range(len(crutch_list)):
    if crutch_list[crutch_index] == [[2]] or crutch_list[crutch_index] == [[6]]:
        total *= (crutch_index + 1)
print(total)

# print(merge([1, 3, 5, 2, 4, 8], 0, 5))


# count = 1
# total = 0
# for l, r in comps:
#     valid = recur(l, r)
#     print(valid)
#     total += count if valid else 0
#     count += 1
# print(total)

        
