#Questão 4. Faça um programa que receba o salário-base de um funcionário, calcule e mostre o salário a receber, 
# sabendo-se que esse funcionário tem gratificação de 5% sobre o salário-base e paga imposto de 7% sobre salário-base.

salarioBase = float(input('Digite o salário-base do funcionário: R$'))
gratificação = salarioBase * 0.05
imposto = salarioBase * 0.07
desconto = salarioBase - imposto
novoSalario = desconto + gratificação 

print('O salário do funcionário a receber é R${:.2f}'.format(novoSalario))