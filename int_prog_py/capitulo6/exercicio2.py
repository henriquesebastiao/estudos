# Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.

# Variáveis
lista1 = []
lista2 = []
lista3 = []

# Entrada
for i in range(5):
    lista1.append(int(input('Digite um número para a lista 1: ')))
for i in range(5):
    lista2.append(int(input('Digite um número para a lista 2: ')))

# Processamento
for i in range(5):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

# Saída
print(f'Lista 1: {lista1}')
print(f'Lista 2: {lista2}')
print(f'Lista 3: {lista3}')
