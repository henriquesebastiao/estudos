# Escreva um programa que verifique se um número é palíndromo. Um número palíndromo é aquele que ao ser escrito da
# direita para a esquerda tem o mesmo valor quando escrito da esquerda para a direita. Exemplo: 545, 789987, 97379,
# 123454321.

# Variáveis
numero = int(input('Digite um número: '))
numero_invertido = 0
numero_original = numero

# Processamento
while numero > 0:
    numero_invertido = numero_invertido * 10 + numero % 10
    numero = numero // 10

# Saída
if numero_original == numero_invertido:
    print(f'O número {numero_original} é palíndromo.')
else:
    print(f'O número {numero_original} não é palíndromo.')
