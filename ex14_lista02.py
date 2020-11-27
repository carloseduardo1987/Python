print('### Prova de Linguagem de Programação 2 ###')

print('Questão 1. Qual é o valor de x na operação (2 . x = 6 ):')
op1 = input('a) 2\nb) 5\nc) 3\nd) 4\n\nResposta: ')

print('\nQuestão 2. Python é uma linguagem de :')
op2 = input('a) Decisão\nb) Criação\nc) Desenvolvimento\nd) Programação\n\nResposta: ')

print('\nQuestão 3. A estrutura de decisão simples, executa algo somente quando a condição for :')
op3 = input('a) Falsa\nb) Verdadeira\nc) Nula\nd) Nenhuma das opções\n\nResposta: ')

print('\n======= Gabarito da Prova =======')
print('Questão 1: c')
print('Questão 2: d')
print('Questão 3: b')

resp = 0
if op1 == 'c':
    resp += 1
if op2 == 'd':
    resp += 1
if op3 == 'b':
    resp += 1

print('\n===== Resultado Final =====\n')
print(f'Quantidade de questões acertadas: { resp }. ')
