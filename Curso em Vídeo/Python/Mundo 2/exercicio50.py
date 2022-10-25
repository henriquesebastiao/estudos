'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
'''

números = [int(input("Informe um número: ")) for x in range(6)]
pares = [n for n in números if n % 2 == 0]

print(f"A soma dos números pares é {sum(pares)}")