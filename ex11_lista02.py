print("### Identificador de números positivos e negativos ###")
numero = int(input('Digite um número: '))

if numero > 0 :
    sinal = 'Positivo'
elif numero < 0 :
    sinal = 'Negativo'
else :
    sinal = 'Zero '

print(f'O número { numero } é { sinal }.')
