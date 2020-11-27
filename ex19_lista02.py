n = int(input('Informe um numero: '))

if n > 0 :
    text = 'Positivo'
elif n < 0 :
    n = n * -1
    text = n
if n > 0 :
    text = 'Positivo'
else:
    text = 'Zero'
    
print(f'{ n } é { text }.')