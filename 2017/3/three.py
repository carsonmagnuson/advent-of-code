import math
number = int(open('2017/3/input.txt').read())

def part_one(number):
    return (abs ((math.ceil((((math.pow((math.sqrt(number)//1 + 1 if math.sqrt(number)//1 % 2 == 0 else math.sqrt(number)//1 + 2), 2)) - (((math.sqrt(number)//1 + 1 if math.sqrt(number)//1 % 2 == 0 else math.sqrt(number)//1 + 2) - 2)*((math.sqrt(number)//1 + 1 if math.sqrt(number)//1 % 2 == 0 else math.sqrt(number)//1 + 2) - 2)))/4)/2)) - ((number - 1) % (((math.pow((math.sqrt(number)//1 + 1 if math.sqrt(number)//1 % 2 == 0 else math.sqrt(number)//1 + 2), 2)) - (((math.sqrt(number)//1 + 1 if math.sqrt(number)//1 % 2 == 0 else math.sqrt(number)//1 + 2) - 2)*((math.sqrt(number)//1 + 1 if math.sqrt(number)//1 % 2 == 0 else math.sqrt(number)//1 + 2) - 2)))/4)))) + ((math.sqrt(number)//1 + 1 if math.sqrt(number)//1 % 2 == 0 else math.sqrt(number)//1 + 2)//2)

    ## the actual solution I wrote under pressure, trascribed above as one line
    # odd_sqrted_num = math.sqrt(number)//1 + 1 if math.sqrt(number)//1 % 2 == 0 else math.sqrt(number)//1 + 2
    # odd_layer_number = odd_sqrted_num*odd_sqrted_num
   

    # layer_perimeter = odd_layer_number - ((odd_sqrted_num - 2)*(odd_sqrted_num - 2))
    # corner_cutoff = layer_perimeter/4
    # middle_of_side = math.ceil(corner_cutoff/2)


    # side_delta = abs (middle_of_side - ((number - 1) % corner_cutoff))

    # steps = side_delta + (odd_sqrted_num//2)
    # return steps

def part_two(number):
    transforms = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    matrix = [[0 for _ in range(math.ceil(math.sqrt(number)) + 1)] for _ in range(math.ceil(math.sqrt(number)) + 1)]
    pos = [len(matrix)//2, (len(matrix)//2)]
    matrix[pos[1]][pos[0]] = 1
    layer = 1
    
    while True:   
        layer += 2
        perimeter = (layer - 1) * 4 
        for perimeter_count in range(0, perimeter):
            adjaciency_list = []
            if perimeter_count == 0: pos[0] += 1
            elif perimeter_count < perimeter//4: pos[1] -= 1
            elif perimeter_count < perimeter//2: pos[0] -= 1
            elif perimeter_count < perimeter//4 + perimeter//2: pos[1] += 1
            else: pos[0] += 1
            for x_transf, y_transf in transforms: adjaciency_list.append(matrix[pos[1] + y_transf][pos[0] + x_transf])
            next_val = sum(el for el in adjaciency_list)
            if next_val > number: return next_val
            matrix[pos[1]][pos[0]] = next_val

            

            
           
## I have to traverse the array in a circular pattern. I think I can do it based on whats around the number. We can push the position a w a y from other numbers we find around it, that way we don't have bunch of conditionals. Okay actually no. I think there is easier way.
# another idea for calculating out the length of the sides is what Alex told me, the odd-sqrt - 1. Using this we can just count for each side and the increase count per layer.







        





        




print(part_one(number))
print(part_two(number))
