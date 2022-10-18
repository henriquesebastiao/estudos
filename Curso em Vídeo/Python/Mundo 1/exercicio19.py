'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
'''

from random import choice as sortear

alunos = []
for n in range(1, 5):
    alunos.append(input(f'Digite o nome do {n}º aluno: '))

print(f'O aluno escolhido foi {sortear(alunos)}')