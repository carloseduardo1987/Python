#Questão 6. Elaborar um programa que receba uma medida em pés e apresente o valor convertido em metros.

medida = float(input('Informe a medida em pés :'))
pés = 0.3048
metros = medida * pés
print('O valor convertido em metros é {:.1f} metros'.format(metros))