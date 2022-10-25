'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
mostre os 10 primeiros termos dessa progressão.
'''

PRIMEIRO_TERMO = int(input('Informe o primeiro termo da PA: '))
R = int(input('Informe a razão da PA: '))

for termo in range(PRIMEIRO_TERMO, 11, R):
    print(termo, end=' -> ')

print('FIM')