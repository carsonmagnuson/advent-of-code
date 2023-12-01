input = open('input.txt','r').read().splitlines()

def part_one():
    nums = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    summation = []
    for line in input:
        first = 0
        last = 0
        for char in line:
            if char.isdigit():
                if first:
                    last = char
                else:
                    first = char
        if not last:
            last = first
        

        if type(last) == int:
            line = '3' + line + '1'
            last = line[0]
            first = line[-1]

        for num in nums.keys():
            loc = line.find(num)
            if loc > -1 and loc < line.find(first):
                first = num
            
            loc2 = line.rfind(num)
            if loc2 > -1 and loc2 > line.rfind(last):
                last = num


        summation.append(int(str(int(first) if not nums.get(first) else nums[first]) + str(int(last) if not nums.get(last) else nums[last])))
    return summation

        


print(sum(part_one()))
    



        
