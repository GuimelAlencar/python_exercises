# Exercício 5.1.0

'''
Teste de primalidade com funções
'''

def primality_test(number):
    if number < 2:
        is_prime = False
    else:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                return is_prime
    return is_prime

prime_number_group_limit = int(input("Prime number group limit: "))
response = primality_test(prime_number_group_limit)
if response:
    print(f"{prime_number_group_limit} é primo")
else:
    print(f"{prime_number_group_limit} não é primo")
