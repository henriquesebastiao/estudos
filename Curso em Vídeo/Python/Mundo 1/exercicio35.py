'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''

retas = [float(input('Digite o comprimento da reta: ')) for n in range(3)]
if retas[0] < retas[1] + retas[2] and retas[1] < retas[0] + retas[2] and retas[2] < retas[0] + retas[1]:
    print('As retas podem formar um triângulo.')
else:
    print('As retas não podem formar um triângulo.')