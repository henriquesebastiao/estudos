# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    usuario = input("Informe um nome de usuário: ")
    senha = input("Informe uma senha: ")

    if usuario == senha:
        print("ERRO!")
        print("O nome de usuário e a senha não podem ser iguais.")
        print("Tente novamente.")
        print()
    else:
        print("Cadastro realizado :)")
        break
