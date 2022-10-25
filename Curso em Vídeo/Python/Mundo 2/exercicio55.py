'''
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''

peso = []

for x in range(1, 6):
    peso.append(float(input(f'Informe o peso da {x}ª pessoa: ')))

print(f'O maior peso informado foi {max(peso)}Kg')
print(f'O menor peso informado foi {min(peso)}Kg')