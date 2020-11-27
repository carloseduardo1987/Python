print("### Calculadora de parcelas ###")
valor =  float(input('Digite o valor da compra: R$ '))

if valor <= 100 :
    total = valor / 2 
    parcela = 2
elif valor <= 200:
    total = valor / 3
    parcela = 3
elif valor <= 400 :
    total = valor / 4
    parcela = 4
else :
    total = valor / 5
    parcela = 5

print(f'Sua compra pode ser parcelada em {parcela}x de R${ round(total, 2) }')
