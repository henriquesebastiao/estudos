# Escreva um programa que calcule a raiz quadrada de um númeo. Utilize o método de Newton para obter um resultado
# aproximado. Sendo n o número a obter a raiz quadrada, considere a base b = 2. Calcule p usando a fórmula:
# p = (b + n / b) / 2. Agora, calcule o quadrado de p. A cada passo, faça b = p e recalcule p usando a fórmula acima.
# Pare quando a diferença absoluta entre p * p e n for menor que 0.0001.

# Variáveis
numero = int(input('Digite um número: '))
b = 2
p = (b + numero / b) / 2

# Processamento
while abs(p * p - numero) >= 0.0001:
    b = p
    p = (b + numero / b) / 2

# Saída
print(f'A raiz quadrada de {numero} é {p:.2f}.')
