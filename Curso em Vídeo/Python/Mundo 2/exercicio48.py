'''
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3
e que se encontram no intervalo de 1 até 500
'''
soma = 0

for n in range(0, 501, 3):
    if n % 2 != 0:
        soma += n
    else:
        continue

print(soma)