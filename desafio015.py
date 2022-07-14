a = int(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))
c = (a * 60) + (km * 0.15)
print(f'O total a pagar é de R${c:.2f}')