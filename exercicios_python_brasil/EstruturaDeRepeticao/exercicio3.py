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

while passou:
    print("REQUISITOS:")
    print("""
Nome: maior que 3 caracteres
Idade: entre 0 e 150
Salário: maior que zero
Sexo: 'f' ou 'm'
Estado Civil: 's', 'c', 'v', 'd'
    """)

    while True:
        nome = input("Informe um nome: ")
        if len(nome) < 3:
            passou = False

            eInvalido("NOME")
            print("Tente novamente!")
        else:
            break

    while True:
        idade = input("Informe a idade: ")
        if idade.isnumeric():
            idade = int(idade)
            if idade < 0 or idade > 150:
                passou = False

                eInvalido("IDADE")
                print("Tente novamente!")
            else:
                break
        else:
            passou = False

            eInvalido("IDADE")
            print("Tente novamente!")

    while True:
        salario = input("Informe o salário: ")
        try:
            salario = float(salario)
            if salario < 0:
                passou = False

                eInvalido("SALARIO")
                print("Tente novamente!")
            else:
                break
        except:
            passou = False

            eInvalido("SALARIO")
            print("Tente novamente!")

    while True:
        sexo = input("Informe o sexo: ").upper()
        if sexo != "F" and sexo != "M":
            passou = False

            eInvalido("SEXO")
            print("Tente novamente!")
        else:
            break

    while True:
        estados = ["S", "C", "V", "D"]
        estado_civil = input("Informe o estado civil: ").upper()
        if estado_civil not in estados:
            passou = False

            eInvalido("ESTADO CIVIL")
            print("Tente Novamente!")
        else:
            break
