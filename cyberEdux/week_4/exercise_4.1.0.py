# Exercise 1

'''
Faça um programa onde o usuário insere um número inteiro positivo, e o programa 
imprime todos os divisores do mesmo número.
'''

number = int(input("Número: "))

if number == 0:
    print("0 não possui divisores")
else:
    for i in range(1, (number + 1)):
        if number % i == 0:
            print(i)