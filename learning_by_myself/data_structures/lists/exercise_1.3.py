# Exercise 3

'''
Given a list of numbers. write a program to turn every item of a list into 
its square.
'''

def to_square_1(list_of_items):
    squared_item_list = []
    for item in list_of_items:
        squared_item_list.append(item**2)
    return squared_item_list

def to_square_2(list_of_items):
    squared_item_list = [a**2 for a in list_of_items]
    return squared_item_list

numbers_list = [1, 2, 3, 4, 5, 6, 7]

squared_numbers_list_1 = to_square_1(numbers_list)
squared_numbers_list_2 = to_square_2(numbers_list)

print(squared_numbers_list_1)
print(squared_numbers_list_2)