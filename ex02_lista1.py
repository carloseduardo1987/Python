#Questão 2. Faça um programa que receba três notas e seus respectivos pesos, 
# calcule e mostre a média ponderada dessas notas. Exiba, as notas, 
# seus respectivos pesos e a média.

n1 = float(input('Nota 1:'))
p1 = float(input('Peso 1:'))
n2 = float(input('Nota 2:'))
p2 = float(input('Peso 2:'))
n3 = float(input('Nota 3:'))
p3 = float(input('Peso 3:'))
media = (n1*p1+n2*p2+n3*p3)/(p1+p2+p3)
print('Nota 1 {:.1f}\nNota 2 {:.1f}\nNota 3 {:.1f}\nPeso 1 {:.1f}\nPeso 2 {:.1f}\nPeso 3 {:.1f}\nMédia Ponderada {:.2f}'.format(n1,n2,n3,p1,p2,p3,media))