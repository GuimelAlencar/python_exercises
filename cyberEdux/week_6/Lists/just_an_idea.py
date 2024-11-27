def all_possible_combinations(list_1, list_2):
    list_of_combinations = [x + y for x in list_1 for y in list_2]
    return list_of_combinations

first_characters_list = ['A', 'B', 'C']
second_characters_list = ['X', 'Y', 'Z']

list_of_combinations = all_possible_combinations(first_characters_list, second_characters_list)

print(list_of_combinations)