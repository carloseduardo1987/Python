print("### Calculadora do desconto do IR ###")
salario = float(input("Digite o seu salário: R$ "))

if salario <= 1250:
    desconto = 0
elif salario <= 1900:
    desconto = salario * 0.11
elif salario <= 2700:
    desconto = salario * 0.25
else:
    desconto = salario * 0.275

print(f"O desconto do IR é R$ { round(desconto, 2) }")
