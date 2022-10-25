'''
Refaça o exercício 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
'''

retas = [float(input('Digite o comprimento da reta: ')) for n in range(3)]
if retas[0] < retas[1] + retas[2] and retas[1] < retas[0] + retas[2] and retas[2] < retas[0] + retas[1]:
    print('As retas podem formar um triângulo.', end=' ')
    if retas[0] == retas[1] == retas[2]:
        print('Equilátero.')
    elif retas[0] == retas[1] or retas[0] == retas[2] or retas[1] == retas[2]:
        print('Isósceles.')
    else:
        print('Escaleno.')
else:
    print('As retas não podem formar um triângulo.')