'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''

while True:
    letra = input("Informe uma letra: ").upper()
    if letra.isalpha():
        break
    else:
        print("Você não informou uma letra. Tente novamente.")
        print()

if letra == "F":
    print("F - Feminino")
elif letra == "M":
    print("M - Masculino")
else:
    print("A letra não é igual a F ou M.")