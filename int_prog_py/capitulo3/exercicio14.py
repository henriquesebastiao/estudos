# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a
# quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,
# 00 por dia e R$ 0,15 por km rodado.

# Entrada de dados
km = float(input("Digite a quantidade de km percorridos: "))
dias = int(input("Digite a quantidade de dias pelos quais o carro foi alugado: "))

# Processamento
preco = 60 * dias + 0.15 * km

# Saída de dados
print(f"O preço a pagar é: {preco:.2f}")

