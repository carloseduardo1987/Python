print("### Calculadora do imposto de ISS  ###")
valor = float(input("Digite o valor total de serviços: R$ "))

if valor <= 5000:
    valor = valor * 0.04
elif valor <= 10000:
    valor = valor * 0.06
elif valor <= 20000:
    valor = valor * 0.13
else:
    valor = valor * 0.16

print(f"O valor do imposto de ISS é R$ { round(valor, 2) }")
