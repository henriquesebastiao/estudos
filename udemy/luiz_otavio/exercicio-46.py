'''
Exercício 46
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se o nome e idade forem digitados:
    Exiba:
        Seu nome é <nome>
        Seu nome invertido é <nome invertido>
        Seu nome contém (ou não) espaços
        Seu nome tem <número de letras> letras
        A primeir letras do seu nome é <primeira letra>
        A última letra do seu nome é <última letra>
Se nada for digitado:
    Exiba:
        "Desculpe, você não digitou nada."
'''

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
print()

while nome == "" or idade == "" or not idade.isnumeric():
    print("Desculpe, você digitou algo inválido.")
    print()
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    print()

if nome != "" and idade != "":
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    print(f"Seu nome contém espaços? {' ' in nome}")
    
    indice =0
    lista_nome = []
    for i in nome:
        if i.isspace():
            indice += 1
            continue
        else:
            lista_nome.append(i)
            indice += 1
    print(f"Seu nome tem {len(lista_nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A última letra do seu nome é {nome[-1]}")