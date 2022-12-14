# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

# Entrada de dados
salario = float(input("Digite o salário do funcionário: "))
aumento = 0

# Processamento
if salario > 1250:
    aumento = salario * 0.1
else:
    aumento = salario * 0.15

# Saída de dados
print(f"O aumento é de: {aumento:.2f}")
