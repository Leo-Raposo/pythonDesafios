from datetime import date

totmaior = 0
totmenor = 0
for a in range(1, 8):
    ano = int(input(f'Em que anp a {a}ª nasceu: '))
    idade = date.today().year - ano
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade')
print(f'Ao todo tivemos {totmenor} pessoas menores de idade')
