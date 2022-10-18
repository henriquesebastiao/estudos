'''
Crie um programa que leia dois números e mostre a soma entre eles.
'''

números = [int(input('Digite um número: ')) for n in range(2)]
print(f'A soma entre {números[0]} e {números[1]} é {sum(números)}.')