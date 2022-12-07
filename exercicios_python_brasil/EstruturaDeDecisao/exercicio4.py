'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''

while True:
    letra = input("Informe uma letra: ").upper()
    if letra.isalpha():
        break
    else:
        print("Você não informou uma letra. Tente novamente.")
        print()

vogais = ["A", "E", "I", "O", "U"]

if letra in vogais:
    print(f"A letra {letra} é uma vogal.")
else:
    print(f"A letra {letra} é uma consoante.")