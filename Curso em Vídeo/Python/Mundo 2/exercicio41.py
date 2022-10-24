'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER
'''

from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Digite o ano de nascimento: '))

if ano_atual - ano_nascimento <= 9:
    print('MIRIM')
elif ano_atual - ano_nascimento <= 14:
    print('INFANTIL')
elif ano_atual - ano_nascimento <= 19:
    print('JÚNIOR')
elif ano_atual - ano_nascimento <= 25:
    print('SÊNIOR')
else:
    print('MASTER')