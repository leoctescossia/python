km = float(input("Digite quantos KM você rodou: \n"))
dias = float(input("Quantidade de dias alugados: \n"))
dia_alugado = dias * 60
km_rodado = km * 0.15
print("Preço por dia alugado : ",dia_alugado)
print("Preço por KM rodado : ",km_rodado)
print("Preço Total : ",dia_alugado + km_rodado)