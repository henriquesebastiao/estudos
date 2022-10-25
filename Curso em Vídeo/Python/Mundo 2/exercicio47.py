'''
Crie um programa que mostre na tela todos os os números pares que estão no intervalo entre 1 a 50.
'''
# Listando os números de 1 a 50
for n in range(1, 51):
    
    # Se o número for par, imprima ele na tela
    if n % 2 == 0:
        print(n)
    else:
        continue