'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''

import math
angulo = float(input('Digite o ângulo que você deseja: '))

#A função math.radians() converte o ângulo de graus para radianos
#A função math.sin() calcula o seno de um ângulo de x radianos
print(f'O ângulo de {angulo} tem o SENO de {math.sin(math.radians(angulo)):.2f}')
print(f'O ângulo de {angulo} tem o COSSENO de {math.cos(math.radians(angulo)):.2f}')
print(f'O ângulo de {angulo} tem a TANGENTE de {math.tan(math.radians(angulo)):.2f}')