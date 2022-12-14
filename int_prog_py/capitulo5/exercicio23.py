# Escreva um programa que leia um número e verifique se ele é primo. Para fazer essa verificação, calcule o resto da
# divisão do número por 2 e depois por todos os números ímpares até o número lido. Se o resto de uma dessas divisões
# for igual a zero, o número não é primo. Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.

# Variáveis
numero = int(input('Digite um número: '))
primo = True

# Processamento
if numero == 0 or numero == 1:
    primo = False
elif numero == 2:
    primo = True
else:
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break

# Saída
if primo:
    print(f'O número {numero} é primo.')
else:
    print(f'O número {numero} não é primo.')