ano = int(input('Digite o ano do seu nascimento: '))

idade = 2022 - ano
a = idade - 18
b = 18 - idade

if idade < 18:
    print(f'Você tem \33[1:30:42m{idade} anos!\33[m Ainda não está na hora de se alistar, faltam {b} anos!')
elif idade == 18:
    print(f'Você tem \33[1:30:42m{idade} anos!\33[m Está na hora de se alistar!')
else:
    print(f'Você tem \33[1:30:42m{idade} anos!\33[m  Se passou {a} anos do alistamento, procure o serviço Militar para mais informações!!!')
