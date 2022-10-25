'''
Refaça o exercício 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for
'''

n = int(input("Informe um número: "))

for x in range(1, 11):
    print(f"{n} x {x} = {n * x}")