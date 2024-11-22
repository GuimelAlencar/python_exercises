# Exercício 5.1.1

'''
Faça um programa em que o usuário informe um numero inteiro positivo N e obtênha todos os numeros primos de 2
até o próprio N como saída.
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

for i in range(2, prime_number_group_limit):
    # O erro que enfrentei se dava pelo fato de eu chamar a função repetidas vezes
    # com o prime_number_group_limit, e não o i.
    response = primality_test(i)
    if response:
        print(i)