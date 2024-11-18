# Exercise 2.0

'''
Faça uma calculadora de equações do segundo grau para condições ideais.
'''

import math

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

delta = b**2 - 4*a*c

if delta > 0:
    print("There is 2 solutions to this equation.")
    first_solution = (-b + math.sqrt(delta)) / (2*a)
    second_solution = (-b - math.sqrt(delta)) / (2*a)
    print(f"Those are: {first_solution} and {second_solution}")
if delta == 0:
    print("There is just 1 solution to this equation.")
    solution = (-b + math.sqrt(delta)) / (2*a)
    print(f"It is: {solution}")
else: 
    print("There is no solution to this equation.")