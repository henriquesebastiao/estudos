# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e
# que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e
# escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
# mantidas as taxas de crescimento.

a, b, anos = 80000, 200000, 0
while True:
    if a >= b:
        print(f"A população do país A ultrapassou o país B em {anos} anos.")
        break
    else:
        anos += 1
    a += a * 0.03
    b += b * 0.015
