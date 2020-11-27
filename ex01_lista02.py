print("### Calculadora de desconto do INSS ###")
salario = float(input("Digite o valor do seu salário: R$ "))

if salario <= 600:
    total = salario * 0.07
elif salario <= 800:
    total = salario * 0.08
elif salario <= 1200:
    total = salario * 0.09
else:
    total = salario * 0.11

print(f"O desconto é de R$ { round(total, 2) }")
