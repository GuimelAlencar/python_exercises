# Exercise_1

'''
Faça um programa que determina se o número que o usuário digitou é par ou impar
'''

number = int(input("Número: "))

if number == 0:
    print(f"{number} é par")
else:
    if number % 2 == 0:
        print(f"{number} é par")
    else:
        print(f"{number} é impar")

