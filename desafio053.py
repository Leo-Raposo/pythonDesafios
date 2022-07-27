f = str(input('Digite uma Frase: ')).upper().replace(' ', '').strip()
p = f[::-1]
print(f'O inverso de {f} é {p}')
if f == p:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')
