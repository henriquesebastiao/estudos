# Faça um programa que leia e valide as seguintes informações:
#
#     Nome: maior que 3 caracteres;
#     Idade: entre 0 e 150;
#     Salário: maior que zero;
#     Sexo: 'f' ou 'm';
#     Estado Civil: 's', 'c', 'v', 'd';

def eInvalido(valor):
    print(f"O VALOR INFORMADO PARA {valor} É INVÁLIDO!")
    print()


passou = True
invalidos = []

while passou:
    print("REQUISITOS:")
    print("""
Nome: maior que 3 caracteres
Idade: entre 0 e 150
Salário: maior que zero
Sexo: 'f' ou 'm'
Estado Civil: 's', 'c', 'v', 'd'
    """)

    nome = input("Informe um nome: ")
    if len(nome) < 3:
        passou = False
        invalidos.append("Nome")

        eInvalido("NOME")

    idade = input("Informe a idade: ")
    if idade.isnumeric():
        idade = int(idade)
        if idade < 0 or idade > 150:
            passou = False
            invalidos.append("Idade")

            eInvalido("IDADE")
    else:
        passou = False
        invalidos.append("Idade")

        eInvalido("IDADE")

    salario = input("Informe o salário: ")
    try:
        salario = float(salario)
        if salario < 0:
            passou = False
            invalidos.append("Salario")

            eInvalido("SALARIO")
    except:
        passou = False
        invalidos.append("Salario")

        eInvalido("SALARIO")

    sexo = input("Informe o sexo: ").upper()
    if sexo != "F" and sexo != "M":
        passou = False
        invalidos.append("Sexo")

        eInvalido("SEXO")

    estados = ["S", "C", "V", "D"]
    estado_civil = input("Informe o estado civil: ").upper()
    if estado_civil not in estados:
        passou = False
        invalidos.append("ESTADO CIVIL")

        eInvalido("Estado Civil")

    if not passou:
        print()
        print("Os seguintes valores informados são inválidos:")
        for item in invalidos:
            print(item)

    if passou:
        print()
        print("Todos os valores foram aceitos com sucesso!")
        break
