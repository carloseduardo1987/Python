#Questão 5. Faça um programa que receba um número positivo e maior que zero, calcule e mostre:
#O número digitado ao quadrado;
#O número digitado ao cubo;
#A raiz quadrada do número digitado;
#A raiz cúbica do número digitado;
#A soma do quadrado mais o cubo do número digitado.

numero = float(input('Digite um numero positivo e maior que zero :'))
quadrado = pow(numero,2) 
cubo = pow(numero,3)
raiz = numero ** (1/2)
raizCubica = numero ** (1/3)
soma = quadrado + cubo
print('O numero ao quadrado é {}'.format(quadrado))
print('O numero ao cubo é {}'.format(cubo))
print('A raiz quadrada do numero é {:.1f} '.format(raiz))
print('A raiz cúbica do numero é {:.2f}'.format(raizCubica))
print('A soma do numero quadrado {} mais o cubo do numero digitado {} é : {}'.format(quadrado,cubo,soma))