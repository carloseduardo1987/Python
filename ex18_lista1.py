import math

print("### Calculadora de alcance de um projétil ###")
vo = float(input("Digite a velocidade do projétil: "))
ang = float(input("Digite o ângulo entre o cano do canhão e o solo: "))
pi = math.pi
rad = (ang * pi) / 180
g = 9.8

S = (vo * vo / g) * math.sin(2 * rad)

print(f"O alcance do projétil é de { round(S, 3) } metros")
