'''
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles
'''

from time import sleep

print("Começando a contagem regressiva: ")

contador = 10
for s in range(0, 10):
    print(f"{contador}")
    contador -= 1
    
    sleep(1)

print("BOOMMM!")