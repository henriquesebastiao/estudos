'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".
'''

cidade = input('Digite o nome da cidade: ').strip().upper()
if cidade[:5] == 'SANTO':
    print('A cidade começa com o nome Santo.')
else:
    print('A cidade não começa com o nome Santo.')