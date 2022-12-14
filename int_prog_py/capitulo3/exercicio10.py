# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do
# aumento. Exiba o valor do aumento e do novo salário.

# Entrada de dados
salario = float(input("Digite o valor do salário: "))
porcentagem = float(input("Digite a porcentagem do aumento: "))

# Processamento
aumento = salario * (porcentagem / 100)
novo_salario = salario + aumento

# Saída de dados
print(f"O valor do aumento é: {aumento:.2f}")
