def to_upper_case(list_of_characters):    
    new_list_of_characters = []
    for i in range(len(list_of_characters)):
        new_list_of_characters[i] = list_of_characters[i].upper()
    return new_list_of_characters

my_list = ['a', 'b', 'c']
print(f"Before: {my_list}")

my_list = to_upper_case(my_list)

print(f"After:  {my_list}")