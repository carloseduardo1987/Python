print('### Calculadora de operações básicas ###')
n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
print('1- Adição\n2- Subtração\n3- Multiplicação\n4- Divisão')
operacao = int(input('Digite o número da operção desejada: '))

if operacao == 1 :
    total = round(n1 + n2, 2)
elif operacao == 2 :
    total = round(n1 - n2, 2)
elif operacao == 3 :
    total = round(n1 * n2, 2)
elif operacao == 4 :
    if n2 != 0 :
        total = round(n1 / n2, 3)
    else:
        total = 'invalido'
else:
    total = 'invalido'
    
print(f'O resultado da operação é { total }.')