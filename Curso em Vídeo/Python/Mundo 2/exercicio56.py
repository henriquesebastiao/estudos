'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.

No final do programa, mostre:
A média de idade do grupo.
Qual é o nome do homem mais velho.
Quantas mulheres têm menos de 20 anos.
'''

nomes = []
idades = []
sexos = []

for n in range(1, 5):
    nome = input(f"Informe o nome da {n}ª pessoa: ")
    nomes.append(nome)
    
    idade = int(input(f"Informe a idade da {n}ª pessoa: "))
    idades.append(idade)
    
    sexo = input(f"Informe o sexo da {n}ª pessoa, M para masculino e F para feminino: ").upper
    sexos.append(sexo)

# Resolvendo o problema da idade média
print(f"A média de idade do grupo é {sum(idades)}.")

# Resolvendo o problema do homem mais velho
índice = 0
índices_homens = []
for x in sexos:
    if x == "M":
        índices_homens.append(índice)
    índice += 1

if len(índices_homens) == 0:
    print("Não existe nenhum homem no grupo.")
else:
    idade_homens = [].append(idades[índices_homens])
    
    homem_velho = nomes[idades.index(max(idade_homens))]
    print(f"O homem mais velho é o {homem_velho}.")

# Resolvendo o problema
## Zerando o índice
índice = 0
índices_mulheres = []
for x in sexos:
    if x == "F":
        índices_mulheres.append(índice)
    índice += 1

if len(índices_mulheres) == 0:
    print("Não existem mulheres no grupo.")
else:
    mulheres_abaixo20 = 0
    for x in idades[índices_mulheres]:
        if x < 20:
            mulheres_abaixo20 +=1
        print(f"{mulheres_abaixo20} mulheres tem menos de 20 anos.")