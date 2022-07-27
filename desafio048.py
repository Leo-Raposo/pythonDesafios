s = 0
print('=*=' *25)
print('Insira abaixo o intervalo de números que deseja calcular e o seu múltiplo!')
print('=*=' * 25)
i = int(input('Digite o Nº inicial: '))
f = int(input('Digite o º final: '))
i2 = int(input('Digite o multiplo: '))
for c in range(i-1, f+1, i2):
    s += c
print(f'Você digitou {i} a {f}. A soma dos números que são múltiplos de {i2} é:', s)
