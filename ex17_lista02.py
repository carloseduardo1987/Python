print('### Calculadora de IMC ###')
nome = str(input('Informe o seu nome:'))
idade = float(input('Qual é a sua idade:'))
peso = float(input('Qual é o seu peso: (kg)'))
altura = float(input('Qual é sua altura:'))
imc = peso / (altura ** 2)

if imc <= 17 :
    msg = 'Muito abaixo do peso'
elif imc <= 18.5 :
    pmsg = 'Abaixo do peso'
elif imc <= 25 :
    msg = 'Peso normal'
elif imc <= 30 :
    msg = 'Acima do peso'
elif imc <= 35 :
    msg = 'Obesidade I'
elif imc <= 40 :
    msg = 'Obesidade II'
elif imc > 40 :
    msg = 'Obesidade III (morbida)'
else:
    msg = 'Digite novamente'

print(f'{nome} seu IMC é de {round(imc,2)}\n{ msg }')
