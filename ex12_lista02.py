print("### Identificador de números pares e ímpares ###")
numero = int(input('Informe um número: '))

if numero %2 == 0 :
    resultado = 'Par'
else:
    resultado = 'Ímpar'
    
print(f'O número { numero } informado é { resultado }.')
