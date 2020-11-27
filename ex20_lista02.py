print('### Calculadora de média escolar ###')
n1 = float(input('\nInforme a primeira nota bimestral: '))
n2 = float(input('Informe a segundo nota bimestral: '))
n3 = float(input('Informe a terceira nota bimestral: '))
n4 = float(input('Informe a quarta nota bimestral: '))
md1 = (n1+n2+n3+n4)/4

print(f'\nO valor da média obtida pelo aluno foi { round(md1, 2) }')
if md1 >= 7 :
    print('Aprovado')
elif md1 < 7 :
    ne = float(input('\nInforme a quinta nota bimestral: '))
    md2 = (ne + md1)/2
    if md2 >= 5 :
        print('\nAPROVADO EM EXAME')
        print(f'\nO valor da média obtida pelo aluno foi { round(md2, 2) }')
    else :
        print('\nREPROVADO')
        print(f'\nO valor da média obtida pelo aluno foi { round(md2, 2) }')
