import math
number = int(open('2017/3/input.txt').read())

def part_one(number):
    return (abs ((math.ceil((((math.pow((math.sqrt(number)//1 + 1 if math.sqrt(number)//1 % 2 == 0 else math.sqrt(number)//1 + 2), 2)) - (((math.sqrt(number)//1 + 1 if math.sqrt(number)//1 % 2 == 0 else math.sqrt(number)//1 + 2) - 2)*((math.sqrt(number)//1 + 1 if math.sqrt(number)//1 % 2 == 0 else math.sqrt(number)//1 + 2) - 2)))/4)/2)) - ((number - 1) % (((math.pow((math.sqrt(number)//1 + 1 if math.sqrt(number)//1 % 2 == 0 else math.sqrt(number)//1 + 2), 2)) - (((math.sqrt(number)//1 + 1 if math.sqrt(number)//1 % 2 == 0 else math.sqrt(number)//1 + 2) - 2)*((math.sqrt(number)//1 + 1 if math.sqrt(number)//1 % 2 == 0 else math.sqrt(number)//1 + 2) - 2)))/4)))) + ((math.sqrt(number)//1 + 1 if math.sqrt(number)//1 % 2 == 0 else math.sqrt(number)//1 + 2)//2)
    

    # odd_sqrted_num = math.sqrt(number)//1 + 1 if math.sqrt(number)//1 % 2 == 0 else math.sqrt(number)//1 + 2
    # odd_layer_number = odd_sqrted_num*odd_sqrted_num
   

    # layer_perimeter = odd_layer_number - ((odd_sqrted_num - 2)*(odd_sqrted_num - 2))
    # corner_cutoff = layer_perimeter/4
    # middle_of_side = math.ceil(corner_cutoff/2)


    # side_delta = abs (middle_of_side - ((number - 1) % corner_cutoff))

    # steps = side_delta + (odd_sqrted_num//2)
    # return steps

def part_two(number):
    matrix = []

        




print(part_one(number))
