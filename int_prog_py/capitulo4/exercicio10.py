# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh
# consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. Calcule o preço a pagar
# de acordo com a tabela a seguir.

# Residências: R$ 0,40 por kWh
# Comércios: R$ 0,55 por kWh
# Indústrias: R$ 0,60 por kWh

# Entrada de dados
kwh = float(input("Digite a quantidade de kWh consumida: "))
print("Digite o tipo de instalação: R para residências, I para indústrias e C para comércios.")
tipo = input("Digite o tipo de instalação: ")

# Processamento
preco = 0
if tipo == "R":
    preco = kwh * 0.4
elif tipo == "C":
    preco = kwh * 0.55
elif tipo == "I":
    preco = kwh * 0.6
else:
    print("Tipo de instalação inválido!")