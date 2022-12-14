# Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros
# fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro,
# calcule quantos dias de vida um fumante perderá. Exiba o total de dias.

# Entrada de dados
cigarros_por_dia = int(input("Digite a quantidade de cigarros fumados por dia: "))
anos_fumando = int(input("Digite a quantidade de anos fumando: "))

# Processamento
minutos_perdidos_por_cigarro = 10
minutos_perdidos_por_dia = cigarros_por_dia * minutos_perdidos_por_cigarro
minutos_perdidos_por_ano = minutos_perdidos_por_dia * 365
minutos_perdidos_por_anos_fumando = minutos_perdidos_por_ano * anos_fumando
dias_perdidos = minutos_perdidos_por_anos_fumando / 1440

# Saída de dados
print(f"O total de dias perdidos é: {dias_perdidos:.2f}")
