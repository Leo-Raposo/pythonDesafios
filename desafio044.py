p = float(input('Digite o valor do produto: '))
print("""[ 1 ] à vista no Dinheiro ou PIX
[ 2 ] à Vista no Cartão
[ 3 ] em 2x no cartão
[ 4 ] em 3x ou mais no cartão""")
o = int(input('Seleciona a forma de pagamento: '))

d = p - (p * 0.1)
ac = p - (p * 0.05)
c3 = p + (p * 0.2)

if o == 1:
    print(f'O valor a ser pago será R$ {d:.2f}')
elif o == 2:
    print(f'O valor a ser pago será {ac:.2f}')
elif o == 3:
    print(f'O valor a ser pago será {p:.2f}')
elif o == 4:
    print(f'O valor a ser pago será {c3:.2f}')
else:
    print('Número incorreto, favor digitar novamente!')
