# Exercise 8: Extend nested list by adding the sublist

'''
You have given a nested list. Write a program to extend it by adding the sublist
["h", "i", "j"] in such a way that it will look like the following list.

Given List:
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

Sub list to add:
sub_list = ["h", "i", "j"]

Expected Output:
['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
'''

my_list = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

sub_list = ["h", "i", "j"]

my_list[2][1][2].extend(sub_list)

print(my_list)