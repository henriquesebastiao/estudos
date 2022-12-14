# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
# da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que
# ela não pode exceder 30% do salário ou então o empréstimo será negado.

# Entrada de dados
valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o salário do comprador: "))
anos = int(input("Digite em quantos anos o comprador vai pagar: "))

# Processamento
prestacao = valor_casa / (anos * 12)
if prestacao > salario * 0.3:
    print("Empréstimo negado")
else:
    print("Empréstimo aprovado")
