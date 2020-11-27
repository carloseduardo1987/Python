#Questão 9. Um trabalhador recebeu seu salário e o depositou em sua conta corrente bancária. 
# Esse trabalhador emitiu dois cheques e agora deseja saber seu saldo atual. 
# Sabe-se que cada operação bancária de retirada paga CPMF de 0,38% 
# e o saldo inicial da conta está zerado.

valorConta = 0
cheque = 2
imposto = 0.38
saldo = valorConta - (cheque * imposto )
print('O saldo atual da sua conta bancaria é R${:.2f}'.format(saldo))
