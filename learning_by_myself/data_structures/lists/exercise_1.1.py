# Exercise_1: Reverse a list in Python

# Iput: list_1 = [100, 200, 300, 400, 500]

# Expected output: list_2 = [500, 400, 300, 200, 100]

def list_rollback_1(original_list):
    rollbacked_list = []
    
    for i in range(0, len(original_list)):
        rollbacked_list.append(original_list[(-1 - i)])
        
    return rollbacked_list

def list_rollback_2(original_list):
    return original_list[::-1]

def list_rollback_3(original_list):
    return list(reversed(original_list))

list_1 = [100, 200, 300, 400, 500]

rollbacked_list_1 = list_rollback_1(list_1)
rollbacked_list_2 = list_rollback_2(list_1)
rollbacked_list_3 = list_rollback_3(list_1)

print(rollbacked_list_1)
print(rollbacked_list_2)
print(rollbacked_list_3)