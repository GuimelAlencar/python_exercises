# Exercise 6: Copy specific elements from one tuple to a new tuple

'''
Write a program to copy elements 44 and 55 from the following tuple into a new tuple.

Given:
tuple1 = (11, 22, 33, 44, 55, 66)

Expected output:
tuple2: (44, 55)
'''

my_tuple = (11, 22, 33, 44, 55, 66)

index_1 = my_tuple.index(44)
index_2 = my_tuple.index(55)

tuple_1 = (my_tuple[index_1], my_tuple[index_2])

print(tuple_1)
