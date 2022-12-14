# Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem
# dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5,00 por km acima de 80 km/h.

# Entrada de dados
velocidade = float(input("Digite a velocidade do carro: "))
multa = 0

# Processamento
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f"Você foi multado em R$ {multa:.2f}")
else:
    print("Você não foi multado")
