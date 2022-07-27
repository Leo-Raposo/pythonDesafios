from random import randint
from time import sleep
print('VAMOS JOGAR JOKENPÔ? FAÇA SUA ESCOLHA!!!')
itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
print("""[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura""")
while (True):
    eu = int(input('Selecione a opção: '))
    if eu < 0 or eu >= 3:
        print('JOGADA INVÁLIDA! TENTE NOVAMENTE!')
    else:
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PÔ!!!')
        sleep(0.5)
        print('*~' * 12)
        print(f'Computador jogou {itens[pc]}')
        print(f'Jogador jogou {itens[eu]}')
        print('*~' * 12)
    if pc == 0: #PC jogou PEDRA
        if eu == 0:
            print('EMPATE')
        elif eu == 1:
            print('JOGADOR VENCE')
        elif eu == 2:
            print('COMPUTADOR VENCE')
    elif pc == 1: #PC jogou PAPEL
        if eu == 0:
            print('COMPUTADOR VENCE')
        elif eu == 1:
            print('EMPATE')
        elif eu == 2:
            print('JOGADOR VENCE')
    elif pc == 2: #PC jogou TESOURA
        if eu == 0:
            print('O JOGADOR VENCE')
        elif eu == 1:
            print('COMPUTADOR VENCE')
        elif eu == 2:
            print('EMPATE')
