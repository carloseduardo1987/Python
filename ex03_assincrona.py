# Questão3: Conte quantas vogais tem em seu nome completo e em sua cidade de nascimento.
#  Exiba, seu nome completo e a cidade, e também, quais são as vogais,
#  e a quantidade de cada uma e a quantidade total de vogais. Utilize métodos de listas, strings, etc

nome = input('Informe seu nome completo:\n').lower()
cidade = input('\nInforme a cidade de nascimento:\n').lower()
vogaisNome = 0
vogaisCidade = 0

for caracter in nome:
    if caracter in 'aeiou':
      vogaisNome+= 1
for caracter in cidade:
    if caracter in 'aeiou':
      vogaisCidade+= 1

print('\n\n')
print(f'Seu nome completo é :\n\n>>> {nome}\n\n')
print(f'Vogal (a) em nome é = ', nome.count('a'))
print(f'Vogal (e) em nome é = ', nome.count('e'))
print(f'Vogal (i) em nome é = ', nome.count('i'))
print(f'Vogal (o) em nome é = ', nome.count('o'))
print(f'Vogal (u) em nome é = ', nome.count('u'))
print (f'\n>>> Total Vogais em nome = {vogaisNome}')
print('\n\n')
print(f'Sua cidade natal é :\n\n>>> {cidade}\n\n')
print(f'Vogal (a) em cidade é = ', cidade.count('a'))
print(f'Vogal (e) em cidade é = ', cidade.count('e'))
print(f'Vogal (i) em cidade é = ', cidade.count('i'))
print(f'Vogal (o) em cidade é = ', cidade.count('o'))
print(f'Vogal (u) em cidade é = ', cidade.count('u'))
print (f'\n>>> Total Vogais em cidade = {vogaisCidade}')