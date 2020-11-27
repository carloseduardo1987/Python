#Questão 10. Pedro comprou um saco de ração com peso em quilos. 
# Pedro possui dois gatos para os quais fornece a quantidade de ração em gramas. 
# Faça um programa que receba o peso do saco de ração e a quantidade de ração fornecida para cada gato. 
# Calcule e mostre quanto restará de ração no saco após cinco dias.

peso_saco = float(input('Informe o peso do saco de ração em kg:'))
gato1 = float(input('Informe a quantidade de ração para o primeiro gato :'))
gato2 = float(input('Informe a quantidade de ração para o segundo gato :'))
racao_gramas = peso_saco * 1000
quantidade_racao = (gato1 + gato2)
resta_no_saco = (racao_gramas -(quantidade_racao * 5 ) / 1000)
total = resta_no_saco / 1000
print('Após cinco dias restará {:.2f} kg de ração'.format(total))






