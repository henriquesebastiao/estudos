'''
Escreva que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''

números = [int(input('Digite um número inteiro: ')) for x in range(2)]

if números[0] > números[1]:
    print('O primeiro valor é maior')
elif números[0] < números[1]:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')