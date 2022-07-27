n = int(input('Digite um número inteiro: '))
print('~~*' * 10)
print(f'A tabuada de {n} é:')
print('~~*' * 10)
for n1 in range(1, 11):
    print(f'{n} x {n1} = {n * n1}')
print('~~*' * 10)