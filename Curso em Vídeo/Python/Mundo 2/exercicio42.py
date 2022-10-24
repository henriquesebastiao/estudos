'''
Refaça o exercício 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
'''

restas = [float(input('Digite o comprimento da reta: ')) for n in range(3)]
if restas[0] < restas[1] + restas[2] and restas[1] < restas[0] + restas[2] and restas[2] < restas[0] + restas[1]:
    print('As retas podem formar um triângulo.', end=' ')
    if restas[0] == restas[1] == restas[2]:
        print('Equilátero.')
    elif restas[0] == restas[1] or restas[0] == restas[2] or restas[1] == restas[2]:
        print('Isósceles.')
    else:
        print('Escaleno.')
else:
    print('As retas não podem formar um triângulo.')