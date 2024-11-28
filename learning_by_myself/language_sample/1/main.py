from numbers import list_of_numbers, tuple_of_numbers, set_of_numbers
# import numbers
# import numbers as nums
# from numbers import list_of_numbers as num_lists

from validations import is_even, is_prime, is_even, is_square
# from validations as valid import *
# from validations import is_even as is_this_number_even

def sub_list_of_numbers(list_of_numbers, validation_function, validation_default_value):
    sub_list = []
    for number in list_of_numbers:
        if validation_default_value:
            if validation_function(number) == True:
                sub_list.append(number)
        elif not validation_default_value:
            if validation_function(number) == False:
                sub_list.append(number)
    return sub_list

def sub_tuple_of_numbers(tuple_of_numbers, validation_function, validation_default_value):
    sub_list = []
    for number in tuple_of_numbers:
        if validation_default_value:
            if validation_function(number) == True:
                sub_list.append(number)
        elif not validation_default_value:
            if validation_function(number) == False:
                sub_list.append(number)
    sub_tuple = tuple(sub_list)
    return sub_tuple

def sub_set_of_numbers(set_of_numbers, validation_function, validation_default_value):
    sub_set = set()
    # sub_set = {} Will create a dictionary, not a set 

    for number in set_of_numbers:
        if validation_default_value:
            if validation_function(number) == True:
                sub_set.add(number)
        elif not validation_default_value:
            if validation_function(number) == False:
                sub_set.add(number)
    return sub_set

print(f"List of numbers: {list_of_numbers}")
print(f"Tuple of numbers: {tuple_of_numbers}")
print(f"Set of numbers: {set_of_numbers}")

print(f"List of prime numbers: {sub_list_of_numbers(list_of_numbers, is_prime, True)}")

print(f"Tuple of even numbers: {sub_tuple_of_numbers(tuple_of_numbers, is_even, True)}")
print(f"Tuple of odd numbers: {sub_tuple_of_numbers(tuple_of_numbers, is_even, False)}")

print(f"Set of square numbers: {sub_set_of_numbers(set_of_numbers, is_square, True)}")
