'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

números = [int(input('Digite um número: ')) for n in range(3)]
print(f'O maior número é {max(números)} e o menor é {min(números)}.')