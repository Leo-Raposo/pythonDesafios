from datetime import date
ano = int(input('Digite o ano do seu nascimento: '))
data = date.today().year
idade = data - ano
if ano > data:
    print('Por favor insira uma data válida!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Você tem \33[1:30:42m{idade} anos!\33[m Ainda não está na hora de se alistar, faltam {saldo} anos!')
    a = data + saldo
    print(f'Seu alistamento será em {a}')
elif idade == 18:
    print(f'Você tem \33[1:30:42m{idade} anos!\33[m Está na hora de se alistar!')
elif idade > 18:
    saldo = idade - 18
    print(f'Você tem \33[1:30:42m{idade} anos!\33[m  Se passaram {saldo} anos do alistamento!')
    a = data - saldo
    print(f'Seus alistamento foi em {a}')

