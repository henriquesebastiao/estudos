# Escreva um programa que exiba uma lista de opções (menu): adição, subtração, multiplicação, divisão e sair.
# Imprima a tabuada da operação escolhida. Repita até que a opção sair seja escolhida.

# Variáveis
opcao = 0

# Processamento
while opcao != 5:
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Sair')
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        for i in range(1, 11):
            print(f'1 + {i} = {1 + i}')
            print()
    elif opcao == 2:
        for i in range(1, 11):
            print(f'1 - {i} = {1 - i}')
            print()
    elif opcao == 3:
        for i in range(1, 11):
            print(f'1 x {i} = {1 * i}')
            print()
    elif opcao == 4:
        for i in range(1, 11):
            print(f'1 / {i} = {1 / i}')
            print()
    elif opcao == 5:
        print('Saindo...')
        break
    else:
        print('Opção inválida!')
        print()
