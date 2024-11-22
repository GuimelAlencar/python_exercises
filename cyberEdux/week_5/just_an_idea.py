import math
import random

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
    
def is_multiple(number)

def sub_list_of_numbers(list_of_numbers, validation_function, validation_default_value):
    list_of_a_sub_set = []
    for item in list_of_numbers:
        if validation_default_value:
            if validation_function(item):
                list_of_a_sub_set.append(item)
        elif not validation_default_value:
            if not validation_function(item):
                list_of_a_sub_set.append(item)
    return list_of_a_sub_set

list_of_numbers = list(range(1, random.randrange(10, 100)))

print(f"List of numbers: {list_of_numbers}")

print(f"List of even numbers: {sub_list_of_numbers(list_of_numbers, is_even, True)}")

print(f"List of odd numbers: {sub_list_of_numbers(list_of_numbers, is_even, False)}")

print(f"List of prime numbers: {sub_list_of_numbers(list_of_numbers, is_prime, True)}")

print(f"List of square numbers: {sub_list_of_numbers(list_of_numbers, is_square, True)}")