#Questão 20. Escreva um programa que calcule e exiba na tela o perímetro e área de uma circunferência. 
# Dados: area = Pi raio ** 2, perimetro = 2 Pi * raio.

raio = float(input('Informe o raio de uma circunferência:'))
pi = 3.14
area = pi * (raio ** 2)
perimetro = 2 * (pi * raio)
print('perimetro = {:.2f}'.format(perimetro))
print('Area da circunferência = {:.2f}'.format(area))


