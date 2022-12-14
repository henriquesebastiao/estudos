# Escreva um programa que pergunta a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem,
# cobrando R$ 0,50 por km para viagens de até 200 km, e R$ 0,45 para viagens mais longas.

# Entrada de dados
distancia = float(input("Digite a distância a percorrer: "))
preco = 0

# Processamento
if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45

# Saída de dados
print(f"O preço da passagem é: {preco:.2f}")
