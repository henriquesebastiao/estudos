# Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o
# preço a pagar.

# Entrada de dados
preco = float(input("Digite o preço da mercadoria: "))
porcentagem = float(input("Digite a porcentagem de desconto: "))

# Processamento
desconto = preco * (porcentagem / 100)
preco_a_pagar = preco - desconto

# Saída de dados
print(f"O valor do desconto é: {desconto:.2f}")
