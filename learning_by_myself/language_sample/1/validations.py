import math

def is_even(number):
    if number % 2 == 0:
        return True
    else: 
        return False

def is_prime(number):
    if number < 2:
        return False
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    
def is_square(number):
    if math.sqrt(number) % 1 == 0:
        return True
    else:
        return False
