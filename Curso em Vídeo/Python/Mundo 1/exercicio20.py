'''
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''

from random import shuffle

alunos = []
for n in range(1, 5):
    alunos.append(input(f'Digite o nome do {n}º aluno: '))

shuffle(alunos)
alunos_novo = ''
cont = len(alunos)

for i in alunos:
    alunos_novo += f'{i}'

alunos_novo = ', '.join(alunos_novo)
print(f'A ordem de apresentação será: {alunos_novo}')