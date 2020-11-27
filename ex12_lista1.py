#Questão 12. Criar um programa que efetue o cálculo da hora aula líquida
#  (descontado o percentual de imposto) de um professor. 
# Os dados fornecidos serão: valor da hora aula,
#  número de aulas dadas no mês e percentual de desconto do INSS.¶



horaAula = float(input('Informe o valor da hora aula: R$'))
aulaDadas = float(input('Informe o numero de aulas dadas no mês:'))
desconto = float(input('Informe o percentual de desconto no INSS:'))

salarioBruto = horaAula * aulaDadas   
imposto = salarioBruto * desconto /100
salarioLiquido = salarioBruto - imposto

print('O salário bruto é R${:.2f}'.format(salarioBruto))
print('O valor de desconto é R${:.2f}'.format(imposto))
print('O salário liquido é R${:.2f}'.format(salarioLiquido))