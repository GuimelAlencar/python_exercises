# Exercise 5: Swap two tuples in Python

'''
Given:
tuple1 = (11, 22)
tuple2 = (99, 88)

Expected output:
tuple1: (99, 88)
tuple2: (11, 22)
'''

tuple1 = (11, 22)
tuple2 = (99, 88)

tuple1, tuple2 = tuple2, tuple1
''' 
Ou:
swap = tuple1
tuple1 = tuple2
tuple2 = swap
'''
print(f"tuple1: {tuple1}")
print(f"tuple2: {tuple2}")