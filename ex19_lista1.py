#Questão 19. Efetuar o cálculo e apresentar o valor de uma prestação de um bem em atraso,
#  utilizando a fórmula:
#  prestacao = valor + (valor (taxa / 100) tempo)

valor =  float(input('Informe o valor da prestação do imóvel: R$'))
taxa  = float(input('Informe a taxa para prestação em atraso: R$'))
tempo = float(input('Informe os dias em atraso:'))
prestacao = valor + ( valor * ( taxa / 100) * tempo)
print('O valor da prestação atrasada atualizada é R${:.2F}'.format(prestacao))