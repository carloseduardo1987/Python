print("### Calculadora de comissão ###")
valorMensal = float(input('Digite o volume mensal de vendas: R$ '))

if valorMensal <= 5000:
    total = valorMensal * 0.02
elif valorMensal <= 10000:
    total = valorMensal * 0.05
elif valorMensal <= 15000:
    total = valorMensal * 0.07
else: 
    total = valorMensal * 0.09

print(f'A comissão será de R$ { round(total, 2) }')
