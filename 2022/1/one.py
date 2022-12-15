big, total, totals = 0, 0, []
for calories in open("2022/1/input.txt","r").readlines():
    if calories.strip() == '':
        big = max(total, big)
        totals.append(total)
        total = 0
    else:
        total += int(calories[:len(calories)-1])
totals.sort(reverse=True)
print(f'biggest = {big} and three biggest are {sum(totals[:3])}')

# exec("big, total, totals = 0, 0, []\nfor calories in open('2022/1/input.txt','r').readlines():\n\tif calories.strip() == '':\n\t\tbig = max(total, big)\n\t\ttotals.append(total)\n\t\ttotal = 0\n\telse:\n\t\ttotal += int(calories[:len(calories)-1])\ntotals.sort(reverse=True)\nprint(f'biggest = {big} and three biggest are {sum(totals[:3])}')")
