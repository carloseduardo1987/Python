#Questão 15. Elabore um programa que permita a entrada de dois valores ( x, y ), 
# troque seus valores entre si e então exiba os novos resultados.

x = int(input('Informe o valor de x:'))
y = int(input('Informe o valor de y:'))
aux = x
x = y
y = aux
print('a = {} e b = {}'.format(x,y))
