tipo = input("Digite o tipo do produto: ")
preco = float(input("Digite o preço do produto: R$ "))

if tipo == "Cesta básica":
    total = 0
elif tipo == "Eletrônicos":
    total = preco * 0.25
elif tipo == "Serviços":
    total = preco * 0.18
else:
    total = preco * 0.12

print(f"O valor do imposto é R$ { round(total, 2) }")
