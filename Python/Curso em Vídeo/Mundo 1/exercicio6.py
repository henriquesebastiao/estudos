'''
Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada.
'''
from math import isqrt

num = int(input('Digite um número: '))
print(f'O dobro de {num} é {num * 2}, o triplo é {num * 3} e a raiz quadrada é {isqrt(num)}.')