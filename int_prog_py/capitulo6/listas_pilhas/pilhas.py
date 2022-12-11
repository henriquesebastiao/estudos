# Pilha de pratos

prato = 5
pilha = list(range(1, prato + 1))
while True:
    print(f"\nExistem {len(pilha)} pratos na pilha")
    print(f"Pilha atual: {pilha}")
    print("Digite E para empilhar um novo prato,")
    print("ou D para desempilhar. S para sair.")
    operacao = input("Operação (E, D ou S): ").upper()
    if operacao == "E":
        # Empilhar um novo prato
        prato += 1
        pilha.append(prato)
    elif operacao == "D":
        if len(pilha) > 0:
            lavado = pilha.pop(-1)
            print(f"Prato {lavado} lavado")
        else:
            print("Não há pratos na pilha!")
    elif operacao == "S":
        break
    else:
        print("Operação inválida! Digite apenas E, D ou S!")
