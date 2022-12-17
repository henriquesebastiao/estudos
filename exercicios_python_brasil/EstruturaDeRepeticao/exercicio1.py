# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
# pedindo até que o usuário informe um valor válido.

while True:
    nota = input("Informe uma nota de 0 a 10: ")

    if nota.isnumeric() and (int(nota) >= 0) and (int(nota) <= 10):
        print("O valor foi aceito :)")
        break
    else:
        print("Valor inválido. Tente novamente.")
        print()
