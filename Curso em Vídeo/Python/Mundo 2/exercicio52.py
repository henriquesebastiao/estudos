'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''

num = int(input('Informe um número inteiro: '))

if num > 1:
    for x in range(2, num):
        if num % x == 0:
            print(f'{num} não é primo')
            break
        else:
            print(f'{num} é primo')
            break
else:
    print(f'{num} não é primo')