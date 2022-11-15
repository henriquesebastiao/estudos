'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). 
'''

tamanho = float(input("Informe o tamanho do arquivo para download (em MB): "))
velocidade = float(input("Informe a velocidade do link de Internet (em Mbps): "))
print(f"O tempo aproximado de download do arquivo usando este link é: {(tamanho / 8) / velocidade * 60} minutos.")