#Questão 8. Faça um programa que receba o número de horas trabalhadas e o valor do salário mínimo. 
# Calcule e mostre o salário a receber seguindo as regras abaixo:
#a hora trabalhada vale a metade do salário mínimo;
#o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada;
#o imposto equivale a 3% do salário bruto;
#o salário a receber equivale ao salário bruto menos o imposto.


horasTrabalhadas = float(input('Informe o número de horas trabalhadas:'))
salarioMinimo = float(input('Informe o valor do salário minimo: R$'))
valorHora = salarioMinimo / 2
salarioBruto = horasTrabalhadas * valorHora
imposto = salarioBruto * 0.03
novoSalario = salarioBruto - imposto
print('O salário a receber será R${:.2f}'.format(novoSalario))

