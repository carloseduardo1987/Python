#Questão 7. Elaborar um programa que calcule e apresente em metros por segundo o valor da velocidade de um projétil
#  que percorre uma distância em quilômetros a um espaço de tempo em minutos.

distancia = float(input('Informe a distância :'))
tempo = float(input('Informe o tempo :'))
velProjetil = distancia * 1000 / tempo * 60
print('A velocidade que o projetil atingiu foi {:.2f} m/s'.format(velProjetil))

