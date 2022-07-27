lst = []
for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª Pessoa: '))
    lst += [peso]
print('')
print(f'O maior peso foi {max(lst)} Kg')
print(f'O menor peso foi {min(lst)} Kg')
