# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido
# por eles.

numero_um = int(input("Informe um número inteiro: "))
numero_dois = int(input("Informe outro número inteiro: "))

for x in range(numero_um, numero_dois + 1):
    print(x, end=" ")
