# Escreva um programa que lei dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular
# soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.

# Entrada de dados
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")

# Processamento
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    resultado = num1 / num2
else:
    resultado = "Operação inválida"
