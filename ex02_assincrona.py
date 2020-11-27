# Questão2: Criar um programa que utilize a sua idade como número a ser adivinhado.
#  Exiba no final uma mensagem parabenizando o acerto e também a quantidade de vezes que tentou.
#  Dê dicas se deve ser digitado um número maior ou menor.


cont = 1

idade = int(input('Digite qual é minha idade?'))

while idade != 33:
    cont +=  1
    if idade < 33:
        print('\n>>> Digite um numero maior')
    elif idade > 33:
        print('\n>>> Digite um numero menor')
       
    idade = int(input('\nDigite qual é minha idade?')) 

print('\nParabens você acertou ! você tentou {} vezes para acertar'.format(cont))
