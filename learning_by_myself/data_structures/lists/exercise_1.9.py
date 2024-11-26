# Exercise 9: Replace list’s item with new value if found

'''
You have given a Python list. Write a program to find value 20 in the list, and if it is present, 
replace it with 200. Only update the first occurrence of an item.

Given:
list1 = [5, 10, 15, 20, 25, 50, 20]

Expected output:
[5, 10, 15, 200, 25, 50, 20]
'''

my_list = [5, 10, 15, 20, 25, 50, 20]

index = my_list.index(20)

my_list[index] = 200

print(my_list)

'''
First try:

for i in range(0, len(my_list)):
    if my_list[i] == 20:
        my_list[i] = 200
        break

print(my_list)
'''

