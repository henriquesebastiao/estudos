'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER
'''

from datetime import date

ANO_ATUAL = date.today().year
ANO_NASCIMENTO = int(input('Digite o ano de nascimento: '))

if ANO_ATUAL - ANO_NASCIMENTO <= 9:
    print('MIRIM')
elif ANO_ATUAL - ANO_NASCIMENTO <= 14:
    print('INFANTIL')
elif ANO_ATUAL - ANO_NASCIMENTO <= 19:
    print('JÚNIOR')
elif ANO_ATUAL - ANO_NASCIMENTO <= 25:
    print('SÊNIOR')
else:
    print('MASTER')