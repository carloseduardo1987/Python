# Questão 1. Uma empresa decidiu fazer um levantamento 
# em relação aos candidatos que se apresentarem 
# para preenchi- mento de vagas em seu quadro de funcionários.
#  Supondo que você seja o programador dessa empresa, faça um programa que leia,
#  para cada candidato, a idade, o sexo (M ou F), e a experiência no serviço (S ou N).
#  Para encerrar a entrada de dados, digite a idade igual a zero.
#  O programa também deve calcular e mostrar:
# O número de candidatos do sexo feminino.
# O número de candidatos do sexo masculino.
# A idade média dos homens que já tem experiência no serviço.
# A porcentagem dos homens com mais de 45 anos entre o total dos homens.
# O número de mulheres com idade inferior a 21 anos e com experiência no serviço.
# A menor idade entre as mulheres que já tem experiência no serviço.

homem = mulher = cont = media = perc = soma = m_infeiror = idadeAcima45 = menorIdade = 0

while True :
    idade = int(input("Informe a idade ou digite [0] para terminar\n"))
    if idade == 0 :
      break
    sexo = ' '
    while sexo not in 'MFmf':
      sexo = str(input('Informe o sexo (M ou F):\n')).strip().lower()
    exp = ' '
    while exp not in 'SNsn':
      exp = str(input('Experiência no serviço (S ou N):\n')).strip().lower()

    if sexo == 'f':
        mulher += 1
    if sexo == 'm':
        homem += 1

    if exp == 's':
         media += idade
         cont += 1   
         media = media /cont 

    if idade > 45 and sexo == 'm' :
        idadeAcima45 += 1
        perc = idadeAcima45 / homem * 100

    if idade < 21 and sexo == 'f' and exp == 's':
        m_infeiror += 1

    menorIdade = idade

    if idade <= menorIdade:
        menorIdade = idade

print(f'O número de candidatos do sexo feminino é {mulher}') 
print(f'O número de candidatos do sexo masculino é {homem}')
print(f'A idade média dos homens que já tem experiência no serviço é {media:.1f}')
print(f'A porcentagem dos homens com mais de 45 anos entre o total dos homens é {perc}%')
print(f'O número de mulheres com idade inferior a 21 anos e com experiência no serviço é {m_infeiror}')
print(f'A menor idade entre as mulheres que já tem experiência no serviço é {menorIdade}')     