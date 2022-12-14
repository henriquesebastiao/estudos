# Escreva um programa que calcule o resto da divisão inteira entre dois números. Utilize apenas as operações de soma
# e subtração para calcular o resultado.

# Variáveis
dividendo = int(input('Digite o dividendo: '))
divisor = int(input('Digite o divisor: '))
quociente = 0
resto = dividendo

# Processamento
while resto >= divisor:
    resto -= divisor
    quociente += 1

# Saída
print(f'O quociente da divisão de {dividendo} por {divisor} é {quociente} e o resto é {resto}.')
