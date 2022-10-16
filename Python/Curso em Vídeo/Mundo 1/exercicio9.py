'''
Faça um prgrama que leia um número inteiro qualquer e mostre na tela a sua tabuada.
'''

num = int(input('Digite um número: '))
cont = 1
while cont <= 10:
    print(f'{num} x {cont} = {num * cont}')
    cont += 1
