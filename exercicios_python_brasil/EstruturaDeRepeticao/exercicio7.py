# Faça um programa que leia 5 números e informe o maior número.

numeros = []
for x in range(1, 6):
    numeros.append(input("Informe um número: "))

print(f"O maior número informado é o {max(numeros)}")
