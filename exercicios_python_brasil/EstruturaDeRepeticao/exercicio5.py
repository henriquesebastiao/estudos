# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide
# a entrada e permita repetir a operação.

while True:
    a = input("Informe a população do país A: ")
    b = input("Agora informe a população do país B: ")

    if a.isnumeric() and b.isnumeric() and int(a) > 0 and int(b) > 0:
        a, b = int(a), int(b)
        anos = 0
        break
    else:
        print("Os anos informados são inválidos. Tente Novamente")
        print()
while True:
    if a >= b:
        print(f"A população do país A ultrapassou o país B em {anos} anos.")
        break
    else:
        anos += 1
    a += a * 0.03
    b += b * 0.015
