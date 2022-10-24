'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''

from random import randint

jogadas_possíveis = {"pedra": 1, "papel": 2, "tesoura": 3}

print('Selecione a sua jogada:')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
jogada = int(input('Digite a sua jogada: '))
jogada_computador = randint(1, 3)

if jogada not in jogadas_possíveis.values():
    print('Jogada inválida.')
elif jogada == jogada_computador:
    print('Empate.')
    print('Você jogou', list(jogadas_possíveis.keys())[jogada - 1], 'e o computador jogou', list(jogadas_possíveis.keys())[jogada_computador - 1], '.')
elif jogada == 1 and jogada_computador == 3 or jogada == 2 and jogada_computador == 1 or jogada == 3 and jogada_computador == 2:
    print('Você ganhou!')
    print('Você jogou', list(jogadas_possíveis.keys())[jogada - 1], 'e o computador jogou', list(jogadas_possíveis.keys())[jogada_computador - 1], '.')
else:
    print('Você perdeu!')
    print('Você jogou', list(jogadas_possíveis.keys())[jogada - 1], 'e o computador jogou', list(jogadas_possíveis.keys())[jogada_computador - 1], '.')