print("### Calculadora de desconto em compras ###")
valor = float(input('Digite o valor da compra: R$ '))

if valor <= 150 :
    total = valor * 0.05
elif valor <= 300 :
    total = valor * 0.07
elif valor <= 500 :
    total = valor * 0.10
else:
    total = valor * 0.20
    
print(f'O desconto na compra será R${ round(total, 2) }')
