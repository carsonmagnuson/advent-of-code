nine = __import__('9')

input = 1

def test_a():
    input = nine.doparse('input.txt')
    assert input
    assert nine.a(input) == 114


    
    

    
    
