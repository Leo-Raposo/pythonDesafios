s = float(input('Insira o salário que deseja realizar o aumento: '))

s1 = s * (10/100) + s
s2 = s * (15/100) + s
print(f'{s1}')
if s > 1250:
    print(f'Reajuste de 10%, e seu novo salário é R$ {s1}')
else:
    print(f'Reajuste de 15%, e seu novo salário é R$ {s2}')
