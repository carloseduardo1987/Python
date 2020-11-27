#Questão 17. Elabore um programa que calcule e exiba quantas notas de 50, 10 e 1
#  são necessárias para se pagar uma conta cujo valor é fornecido

conta = float(input('Informe o valor da conta a pagar: R$'))
print('Seram necessarias {:.0f} de cédulas de R$50'.format(conta/50))
print('Seram necessarias {:.0f} de cédulas de R$10'.format(conta/10))
print('Seram necessarias {:.0f} de cédulas de R$1'.format(conta/1))
