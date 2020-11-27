#Questão 16. Elabore um programa que calcule e exiba a média aritmética de 5 números ( k, x, y, z, w).

k = float(input('Digite o primeiro número:'))
x = float(input('Digite o segundo número:'))
y = float(input('Digite o terceiro número:'))
z = float(input('Digite o quarto número:'))
w = float(input('Digite o quinto número:'))
media = (k+x+y+z+w) / 5
print('A média aritmética é {:.1f}'.format(media))
