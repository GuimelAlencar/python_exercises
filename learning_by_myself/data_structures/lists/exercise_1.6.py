# Exercise 6: Remove empty strings from the list of strings

'''
Input:
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

Expected output:
["Mike", "Emma", "Kelly", "Brad"]
'''

def list_verification_1(list_1):
    for item in list_1:
        if item == "":
            list_1.remove(item)

def list_verification_2(list_2):
    verificated_list = list(filter(None, list_2))
    return verificated_list

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
list2 = ["Mathew", "", "Mark", "Luke", "", "Jhon"]

list_verification_1(list1)
verificated_list = list_verification_2(list2)

print(list1)
print(verificated_list)
