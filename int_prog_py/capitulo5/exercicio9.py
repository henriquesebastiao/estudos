# Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da
# divisão. Utilize apenas as operações de soma e subtração para calcular o resultado. Lembre-se de que podemos entender
# o quociente da divisão de dois números como a quantidade de vezes que podemos retirar o divisor do dividendo. Logo,
# 20 ÷ 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.

# Entrada de dados
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
quociente = 0
resto = 0

# Processamento
while num1 >= num2:
    num1 = num1 - num2
    quociente = quociente + 1
resto = num1

# Saída de dados
print(f"O quociente da divisão é: {quociente}")
print(f"O resto da divisão é: {resto}")
