# Exercise 3

'''
O usuário vai inserir um número, e o programa deverá imprimir se ele é primo ou não.
'''

number = int(input("Número: "))

if number == 0:
    print("0 não é primo")
elif number == 1:
    print("1 não é primo")
else:
    number_of_divisors = 0
    for i in range(1, (number + 1)):
        if number % i == 0:
            number_of_divisors += 1
    if number_of_divisors == 2:
        print(f"O número {number} é primo")
    else:
        print(f"O número {number} não é primo")