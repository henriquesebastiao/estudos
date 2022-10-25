'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''

VALOR_NORMAL = float(input('Digite o preço normal do produto: '))
print()
print('Selecione a condição de pagamento:')
print('1 - À vista dinheiro/cheque')
print('2 - À vista no cartão')
print('3 - em até 2x no cartão')
print('4 - ou mais no cartão')
condição = int(input('Digite a condição de pagamento: '))

if condição == 1:
    preço_final = VALOR_NORMAL * 0.9
elif condição == 2:
    preço_final = VALOR_NORMAL * 0.95
elif condição == 3:
    preço_final = VALOR_NORMAL
    parcelas = 2
elif condição == 4:
    preço_final = VALOR_NORMAL * 1.2
    parcelas = int(input('Digite o número de parcelas: '))
else:
    print('Condição inválida.')
    exit()

print(f'O preço final do produto é R$ {preço_final:.2f}.')
print(f'Você pagará em {parcelas} parcelas de R$ {preço_final / parcelas:.2f}.')