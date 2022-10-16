'''
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
'''
altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
quant_tinta = area / 2
print(f'A área da parede é de {area}m² e a quantidade de tinta necessária para pintá-la é de {quant_tinta}L')
