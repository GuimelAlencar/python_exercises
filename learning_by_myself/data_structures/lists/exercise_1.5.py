# Exercise 5: Iterate both lists simultaneously

'''
Given a two Python list. Write a program to iterate both lists simultaneously 
and display items from list1 in original order and items from list2 in reverse order.

Given:
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

Expected output:
10 400
20 300
30 200
40 100
'''

def list_rollback(original_list):
    return original_list[::-1]

def concurrent_iteration(list_1, list_2_reverted):
    for item_1, item_2 in zip(list_1, list_2_reverted):
        print(item_1, item_2)

list_1 = [10, 20, 30, 40]
list_2 = [100, 200, 300, 400]

list_2_reverted = list_rollback(list_2)

concurrent_iteration(list_1, list_2_reverted)