# Exercise 3

'''
Faça uma calculadora de imc
'''

weight = float(input("Weight: "))
height = float(input("Height: "))

imc = weight / height**2

if imc < 16:
    print("Desnutrição sesvera!!!")
elif imc > 16 and imc <= 18.4:
    print("Desnutrição moderada!!")
elif imc > 18.4 and imc <= 22:
    print("Abaixo do peso!")
elif imc > 22 and imc <= 24.9:
    print("Peso normal.")
elif imc > 24.9 and imc <= 29.9:
    print("Sobrepeso!")
elif imc > 29.9 and imc <= 34.9:
    print("Obesidade tipo 1!")
elif imc > 34.9 and imc <= 39.9:
    print("Obesidade tipo 2!!")
else:
    print("Obesidade tipo 3!!!")