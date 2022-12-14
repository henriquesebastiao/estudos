# Escreva um programa que converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32

# Entrada de dados
celsius = float(input("Digite a temperatura em Celsius: "))

# Processamento
fahrenheit = 9 * celsius / 5 + 32

# Saída de dados
print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}")
