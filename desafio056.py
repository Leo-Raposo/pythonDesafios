somaidade = 0
mediaidade = 0
maioridade = 0
nomevelho = 0
mulher20 = 0
for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    n = str(input('Digite seu nome: ')).strip()
    i = int(input('Digite sua idade: '))
    s = str(input('Digite seu sexo(M/F): ')).strip()
    somaidade += i
    if c == 1 and s in 'Mm':
        maioridade = i
        nomevelho = n
    if s in 'Mm' and i > maioridade:
        maioridade = i
        nomevelho = n
    if s in 'Ff' and i < 20:
        mulher20 += 1
mediaidade = somaidade / 4
print(f'A media de idado do grupo é de {mediaidade:.0f} anos.')
print(f'O homem mais velho tem {maioridade} anos e se chama {nomevelho}.')
print(f'Ao todo são {mulher20} mulheres com menos de 20 anos.')
