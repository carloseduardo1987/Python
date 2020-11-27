print("### Identificador de Categorias - Natação ###")
idade = int(input('Digite a sua idade: '))

if ( idade >= 5 and idade <= 8 ) :
    categoria = 'Infantil A'
elif ( idade >= 8 and idade <= 10 ) :
    categoria = 'Infantil B'
elif ( idade >= 11 and idade <= 13 ) :
    categoria = 'Juvenil A'
elif ( idade >= 14 and idade <= 17 ) :
    categoria = 'Juvenil B'
elif ( idade > 17 ) :
    categoria = 'Senior'
else:
    categoria = 'Invalida'

print(f'A sua categoria é: { categoria }.')
