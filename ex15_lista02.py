print("### Identificador de tipo de triângulo ###")
lado1 = float(input('Informe o tamanho do primeiro lado do triângulo: '))
lado2 = float(input('Informe o tamanho do segundo lado do triângulo: '))
lado3 = float(input('Informe o tamanho do terceiro lado do triângulo: '))

if  lado1 < lado2 + lado3 and  lado2 <  lado1 + lado3  and  lado3 <  lado1 + lado2 :
   if lado1 == lado2 == lado3:
        tipo = 'Equilátero'
   elif lado1 != lado2 != lado3 != lado1:
        tipo = 'Escaleno'
   else:
        tipo = 'Isósceles'
    print(f'O triângulo é: { tipo }')
else:
    print('Os lados informados não podem formar um triângulo!')
