# https://pynative.com/python-data-structure-exercise-for-beginners/
# https://pynative.com/python-list-exercise-with-solutions/
# https://pynative.com/python-lists/

# Learning Python Lists

# 1. Creating a python list

# 1.1 Using list constructor
my_list1 = list((1, 2, 3))
print(my_list1)
# Output [1, 2, 3]

# 1.2 Using square brackets[]
my_list2 = [1, 2, 3]
print(my_list2)
# Output [1, 2, 3]

# with heterogeneous items
my_list3 = [1.0, 'Jessa', 3]
print(my_list3)
# Output [1.0, 'Jessa', 3]

# empty list using list()
my_list4 = list()
print(my_list4)
# Output []

# empty list using []
my_list5 = []
print(my_list4)
# Output []

# 2. Legth of a list
# In order to find the number of items present in a list, we can use the len() function.

my_list = [1, 2, 3]
print(len(my_list))
# output 3

# 3. Acessing items of a list

# 3.1 Using indexing
my_list = ['A', 'B', 'C']

# 3.1.1 Positive indexing
print(my_list[0])
# output A
print(my_list[1])
# output B
print(my_list[2])
# output C

# 3.1.2 Negative indexing
print(my_list[-1])
# output C
print(my_list[-2])
# output B
print(my_list[-3])
# output A

# print(my_list[10])
# output 'Index error'
# print(my_list['a'])
# output 'Type error'

# 3.2 List slicing
# Syntax: list_name[start_index : end_index : step]

my_list = ['p', 'y', 't', 'h', 'o', 'n']

# 3.2.1 Extract a portion of the list

# first 2 items
print(my_list[0:2])
# output ['p', 'y']

# until index 4
print(my_list[:4])
# output ['p', 'y', 't', 'h']

# by 2
print(my_list[::2])
# output ['p', 't', 'o']

# Backwards
print(my_list[::-1])
# output ['n', 'o', 'h', 't', 'y', 'p']

# Starting from 4nd item
print(my_list[4:])
# output ['o', 'n']

# 3.3 Iterating over a list

# 3.3.1 Iterating using a simple for
my_list = ["Mathew", "Mark", "Luke", "John"]
for item in my_list:
    print(item)
# output Mathew Mark Luke John

# 3.3.2 Iterating along with an index number
for i in range(0, len(my_list)):
    print(my_list[i])
# output Mathew Mark Luke John

# 4. Adding elements to the list

my_list = ["Mathew"]

# 4.1 Append item at the end of the list
my_list.append("Luke")
print(my_list)
# output ['Mathew', 'Luke']

# 4.2 Insert an item in a specified position in the list
# insert(index, object)

# insert "Mark" at position 1
my_list.insert(1, "Mark")
print(my_list)
# output ['Mathew', 'Mark', 'Luke']

# 4.3 Add an list of elements at the end of the actual list

my_list = ["Mathew", "Mark"]
my_list.extend(["Luke", "John"])
print(my_list)
# output ["Mathew", "Mark", "Luke", "John"]

# 5. Modify the itens of a list

# 5.1 Modify a specific item
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list[3] = 300
print(my_list)
# output [0, 1, 2, 100, 4, 5, 6, 7, 8, 9, 10]

# 5.2 modify a s range of items
my_list[6:10] = [600, 700, 800, 900]
print(my_list)
# output [0, 1, 2, 300, 4, 5, 600, 700, 800, 900, 10]

# 5.3 Modify all items
my_list = [2, 4, 6, 8, 10]
for i in range(len(my_list)):
    my_list[i] = my_list[i]**2
print(my_list)
# output [4, 16, 36, 64, 100]

# 6. Removing the items of a list

# 6.1 Removing a specific item of a list
my_list = ['A', 'B', 'C']
my_list.remove('A')
print(my_list)
# return ['B', 'C']

# 6.2 Remove all occurence of a specific item
my_list = ['A', 'B', 'A', 'C', 'A']

for item in my_list:
    my_list.remove('A')
print(my_list)
# return ['B', 'C']

# 6.3 Remove item at given index
my_list = ['A', 'B', 'C']

my_list.pop()
# Removes the last index ('C')

my_list.pop(0)
# Removes the first index
print(my_list)
# output ['B']

# 6.4 Remove a range of items
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del my_list[2:5]
print(my_list)
# output [1, 2, 6, 7, 8, 9]
del my_list[3:]
print(my_list)
# output [1, 2, 6]

# 6.5 Remove all items
my_list = [1, 2, 3]
my_list.clear()
# output []

my_list = [1, 2, 3]
del my_list
# List deleted

# 7. Concatenation of 2 lists

my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]

# Using + operator
my_list3 = my_list1 + my_list2
print(my_list3)
# Output [1, 2, 3, 4, 5, 6]

# Using extend() method
my_list1.extend(my_list2)
print(my_list1)
# Output [1, 2, 3, 4, 5, 6]]]

# 8. Copying lists