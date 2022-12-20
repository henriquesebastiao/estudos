# Faça um programa que leia 5 números e informe a soma e a média dos números.

numeros = []
for x in range(1, 6):
    numeros.append(int(input("Informe um número: ")))

soma = 0
for x in numeros:
    soma += x

print(f"A média dos números informados é: {soma / len(numeros)}")
