# Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0
# (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.

# Entrada de dados
soma = 0
contador = 0

while True:
    num = int(input("Digite um número inteiro: "))
    soma += num
    if num != 0:
        contador += 1
    if num == 0:
        break

# Saída de dados
print(f"A quantidade de números digitados é: {contador}")
print(f"A soma dos números digitados é: {soma}")
print(f"A média aritmética dos números digitados é: {soma / contador:.2f}")
