#Questão 13. Dado um polígono convexo de n lados, podemos 
# calcular o número de diagonais diferentes (nd) desse polígono pela fórmula: nd = n * (n - 3) / 2. 
# Fazer um programa que leia quantos lados tem o polígono, 
# calcule e escreva o número de diagonais diferentes (nd) do mesmo.

n = float(input('Informe quantos lados tem o polígono:'))
nd = n * (n - 3) / 2
print('O numero de diagonais diferentes são {:.1f}'.format(nd))