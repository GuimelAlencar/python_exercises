# Exercise 2

''' 
Write a program to add two lists index-wise. 
Create a new list that contains the 0th index item from both the list, 
then the 1st index item, and so on till the last element. 
any leftover items will get added at the end of the new list.
'''

# Given:
# list_1 = ["M", "na", "i", "Ke"]
# list_2 = ["y", "me", "s", "lly"]
# Expected output: ['My', 'name', 'is', 'Kelly']

def concatenate_lists_by_index_1(list_1,list_2):
    return [a + b for a, b in zip(list_1, list_2)]

def concatenate_lists_by_index_2(list_1,list_2):
    list_concatenated_by_index = []

    zipped_list = zip(list_1,list_2)
    
    for pair_of_items in zipped_list:
        first_item = pair_of_items[0]
        second_item = pair_of_items[1]
        new_item = first_item + second_item
        list_concatenated_by_index.append(new_item)
    
    return list_concatenated_by_index

list_1 = ["M", "na", "i", "Ke"]
list_2 = ["y", "me", "s", "lly"]

list_3 = concatenate_lists_by_index_1(list_1,list_2)
list_4 = concatenate_lists_by_index_2(list_1,list_2)

print(list_3)
print(list_4)
