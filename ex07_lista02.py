print("### Calculadora de juros de empréstimos bancários ###")
valor = float(input('Digite o valor a ser emprestado: R$ '))
parcelas = int(input('Digite o número de parcelas: '))

if parcelas <= 3 :
    total = valor * 0.06
elif parcelas <= 6 :
    total = valor * 0.09
elif parcelas <= 12 :
    total = valor * 0.22
else:
    total = valor * 0.34 

print(f'O valor do juros do emprestimo bancário será R${ round(total, 2) }')
