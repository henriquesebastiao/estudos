'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''

nome = input('Digite o nome da pessoa: ').strip().upper()
if 'SILVA' in nome:
    print('O nome da pessoa contém Silva.')
else:
    print('O nome da pessoa não contém Silva.')