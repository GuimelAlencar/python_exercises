# Exercise 1.0 

'''
Faça um programa em que um professor coloque as 3 notas das avaliações de um aluno, e os pesos das
respectivas notas, porfim, o programa deve imprimir a situação do aluno de acordo com o que se
segue:
1. nota final < 5.0 = Reprovado!
2. 5 > nota final <= 7.0 = Prova Final.
3. nota final > 7.0 = Aprovado.
'''

test_1 = float(input("Test 1: "))
weight_1 = float(input("Weight 1: "))
grade_1 = test_1 * weight_1

test_2 = float(input("Test 2: "))
weight_2 = float(input("Weight 2: "))
grade_2 = test_2 * weight_2

test_3 = float(input("Test 3: "))
weight_3 = float(input("Weight 3: "))
grade_3 = test_3 * weight_3

sum_of_weights = weight_1 + weight_2 + weight_3
sum_of_grades = grade_1 + grade_2 + grade_3

media = sum_of_grades / sum_of_weights
 
if media <= 5:
    print("Reproved!")
elif  media > 5 and media <= 7:
    print("Final test!")
else:
    print("Aproved!")
