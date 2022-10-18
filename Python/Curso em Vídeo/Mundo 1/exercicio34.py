'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''

salário = float(input('Qual o salário do funcionário? R$'))
if salário > 1250:
    aumento = salário * 0.1
else:
    aumento = salário * 0.15

print(f'O salário do funcionário é R${salário + aumento:.2f}')