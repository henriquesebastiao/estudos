'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo:

    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$

    Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

por_hora = float(input("Informe quanto você ganha por hora: "))
horas_trabalhadas = float(input("Informe quantas horas você trabalhou no mês: "))
print(f"O seu salário bruto é: {por_hora * horas_trabalhadas}")
print(f"O INSS é: {por_hora * horas_trabalhadas * 0.08}")
print(f"O sindicato é: {por_hora * horas_trabalhadas * 0.05}")
print(f"O IR é: {por_hora * horas_trabalhadas * 0.11}")
print(f"O salário líquido é: {por_hora * horas_trabalhadas - (por_hora * horas_trabalhadas * 0.08) - (por_hora * horas_trabalhadas * 0.05) - (por_hora * horas_trabalhadas * 0.11)}")