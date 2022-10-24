'''
Escreva um programa que para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''

valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você vai pagar? '))
prestação_mensal = valor / (anos * 12)

if prestação_mensal > salario * 0.3:
    print('Empréstimo negado!')
else:
    print('Empréstimo aprovado!')