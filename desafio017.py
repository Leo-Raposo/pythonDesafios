import math

co = float(input('Insira o valor do cateto oposto: '))
ca = float(input('Insira o valor do cateto adjacente: '))

h = (co * co) + (ca * ca)
hi = math.sqrt(h)

print(f'O Cateto oposto {co:.2f} e o cateto adjacente {ca:.2f} resutam em uma hipotenusa {hi:.2f}')
