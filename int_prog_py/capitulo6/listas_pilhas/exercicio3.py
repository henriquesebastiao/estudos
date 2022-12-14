# Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.

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
    if lista1[i] not in lista3:
        lista3.append(lista1[i])
    if lista2[i] not in lista3:
        lista3.append(lista2[i])

# Saída
print(f'Lista 1: {lista1}')
print(f'Lista 2: {lista2}')
print(f'Lista 3: {lista3}')
