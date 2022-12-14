# Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês
# para os 24 primeiros meses. Escreva o total ganho com juros no período.

# Entrada de dados
deposito_inicial = float(input("Digite o depósito inicial: "))
taxa_juros = float(input("Digite a taxa de juros: "))
meses = 24

# Processamento
for mes in range(1, meses + 1):
    juros = deposito_inicial * taxa_juros / 100
    deposito_inicial += juros
    print(f"Depósito do mês {mes}: {deposito_inicial:.2f}")

# Saída de dados
print(f"Total ganho com juros: {deposito_inicial:.2f}")
