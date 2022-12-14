# Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média
# esperada para a viagem.

# Entrada de dados
distancia = float(input("Digite a distância a percorrer: "))
velocidade = float(input("Digite a velocidade média esperada: "))

# Processamento
tempo = distancia / velocidade

# Saída de dados
print(f"O tempo da viagem é: {tempo:.2f} horas")
