# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo
# número. Não utilize a função de potência da linguagem.

base = int(input("Informe o número da base: "))
expoente = int(input("Informe o número do expoente: "))
resultado = base

while expoente > 0:
    resultado *= base
    expoente -= 1

print(f"O resultado é: {resultado}")
