# Altere o programa anterior para mostrar no final a soma dos números.

numero_um = int(input("Informe um número inteiro: "))
numero_dois = int(input("Informe outro número inteiro: "))
numeros = []
soma = 0

for x in range(numero_um, numero_dois + 1):
    print(x, end=" ")
    print()
    numeros.append(x)

for x in numeros:
    soma += x

print(f"O resultado da some dos números é: {soma}")
