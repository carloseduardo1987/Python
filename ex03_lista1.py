#Questão 3. Faça um programa que receba o salário de um funcionário e o percentual de aumento,
#  calcule e mostre o valor do aumento e o novo salário.

salario = float(input('Informe o sálario do funcionário : R$'))
aumento = float(input('Informe o aumento em porcentagem :'))
aumento = salario * (aumento/100)
novoSalario = aumento + salario
print('O valor do aumento é R${:.2f}'.format(aumento))
print('O valor do novo salário é R${:.2f}'.format(novoSalario))