#Questão 21. Escreva um programa que solicite ao usuário
#  dois números e apresente na tela os resultados das operações aritméticas 
# (soma, subtração, multiplicação, divisão, resto da divisão, exponenciação, radiciação).


n1 = float(input('Digite o primeiro número:'))
n2 = float(input('Digite o segundo número:'))
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
exponenciacao = n1 ** n2
radiciacao = n1 ** (1 / n2)
print('Soma = {:.0f}'.format(soma))
print('Subtração = {:.0f}'.format(subtracao))
print('Multiplicação = {:.0f}'.format(multiplicacao))
print('Divisão = {:.1f}'.format(divisao))
print('Exponenciação = {:.1f}'.format(exponenciacao))
print('Radiciação = {:.1f}'.format(radiciacao))