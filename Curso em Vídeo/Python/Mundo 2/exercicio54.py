'''
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores.
'''
menoridade = 0
maioridade = 0

for x in range(1, 8):
    ano_nascimento = int(input(f'Informe o ano de nascimento da {x}ª pessoa: '))
    idade = 2020 - ano_nascimento
    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1

print(f'{maioridade} pessoas são maiores de idade.')
print(f'{menoridade} pessoas são menores de idade.')