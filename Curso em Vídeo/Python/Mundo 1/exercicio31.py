'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
'''

distância = float(input('Qual a distância da viagem? '))
if distância <= 200:
    preço = distância * 0.5
else:
    preço = distância * 0.45
    
print(f'O preço da passagem é R${preço:.2f}')