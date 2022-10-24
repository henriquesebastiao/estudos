'''
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Digite o ano de nascimento: '))

if ano_atual - ano_nascimento < 18:
    print(f'Ainda faltam {18 - (ano_atual - ano_nascimento)} anos para o alistamento.')
    print(f'Seu alistamento será em {ano_atual + (18 - (ano_atual - ano_nascimento))}')
elif ano_atual - ano_nascimento > 18:
    print(f'Você já deveria ter se alistado há {ano_atual - ano_nascimento - 18} anos.')
    print(f'Seu alistamento foi em {ano_atual - (ano_atual - ano_nascimento - 18)}')
else:
    print('Você tem que se alistar IMEDIATAMENTE!')