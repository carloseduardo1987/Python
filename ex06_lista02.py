print("### Calculadora de desconto na compra do cliente ###")
compra = float(input('Digite o valor da compra: R$ '))

if compra <= 50 :
    total = compra * 0.05
elif compra <= 100 :
    total = compra * 0.08
elif compra <= 150 :
    total = compra * 0.12
else:
    total = compra * 0.15
    
print(f'O valor do desconto na compra do cliente será R${ round (total, 2) }')
