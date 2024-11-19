# Exercise 1

'''
Faça um programa onde o usuário insere um número inteiro positivo, e o programa imprime todos os
divisores do mesmo número.
'''

number = int(input("Número: "))

if number == 0:
    print("0 não possui divisores")
elif number == 1:
    print("1")
else:
    count = 1
    while number >= count:
        if number % count == 0:
            print(count)
        count += 1