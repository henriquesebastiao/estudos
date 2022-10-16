'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Considere US$1,00 = R$3,27
'''

quanto_dinheiro = float(input('Quanto dinheiro você tem na carteira? R$'))
dolares = quanto_dinheiro / 3.27
print(f'Com R${quanto_dinheiro:.2f} você pode comprar US${dolares:.2f}')
