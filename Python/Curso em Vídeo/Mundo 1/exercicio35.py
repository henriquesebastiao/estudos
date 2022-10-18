'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''

restas = [float(input('Digite o comprimento da reta: ')) for n in range(3)]
if restas[0] < restas[1] + restas[2] and restas[1] < restas[0] + restas[2] and restas[2] < restas[0] + restas[1]:
    print('As retas podem formar um triângulo.')
else:
    print('As retas não podem formar um triângulo.')