'''
Crie um programa que leia uma fase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.
'''

frase = str(input('Informe uma frase: ')).strip().upper()

if frase == frase[::-1]:
    print(f'A frase "{frase}" é um palíndromo')
else:
    print(f'A frase "{frase}" não é um palíndromo')