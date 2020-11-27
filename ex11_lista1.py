#Questão 11. Antes de o racionamento de energia ser decretado, quase ninguém falava em quilowatts;
#  mas, agora, todos incorporam essa palavra em seu vocabulário. 
# Sabendo-se que 100 quilowatts de energia custa um sétimo do salário mínimo, 
# fazer um programa que receba o valor do salário mínimo
#  e a quantidade de quilowatts gasta por uma residência e calcule. Imprima:
#o valor em reais de cada quilowatt,
#o valor em reais a ser pago,
#o novo valor a ser pago por essa residência com um desconto de 10%.

minimo = float(input('Informe o valor do salário minimo: R$'))
kw = float(input('Informe a quantidade de quilowatts gasta :'))
custo = (minimo / (7 / 100))
print('1kw custa {:.1f} reais'.format(custo))
print('O preço a ser pago é de {:.2f} reais'.format(custo * kw))
print('Com desconto de 10 porcento o preço fica em R${:.2f}'.format(custo * kw /( 10 * 9)))