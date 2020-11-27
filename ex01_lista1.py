#Questão 1. Faça um programa que receba três notas, calcule e mostre a média aritmética entre elas.
#  Exiba, as notas, e a respectiva média.¶


n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
n3 = float(input('Digite a terceira nota:'))
media = (n1+n2+n3)/3
print('Primeira nota {:.1f}\nSegunda nota {:.1f}\nTerceira nota {:.1f}\nMédia = {:.1f}'.format(n1,n2,n3,media))