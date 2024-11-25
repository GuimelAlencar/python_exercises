# Exercise 4: Concatenate two lists in the following order

'''
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

Expected output: ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
'''

def all_possible_concatenations_between_v1(list_1, list_2):
    new_list = []
    for item_list_1 in list_1:
        for item_list_2 in list_2:
            new_item = item_list_1 + item_list_2
            new_list.append(new_item)
    return new_list

def all_possible_concatenations_between_v2(list_1, list_2):
    new_list = [x + y for x in list_1 for y in list_2]
    return new_list


list_1 = ["Hello ", "take "]
list_2 = ["Dear", "Sir"]

list_3 = all_possible_concatenations_between_v1(list_1, list_2)
list_4 = all_possible_concatenations_between_v2(list_1, list_2)

print(list_3)
print(list_4)