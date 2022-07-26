from random import randint
from time import sleep
print('VAMOS JOGAR JOKENPÔ? FAÇA SUA ESCOLHA!!!')
itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
print("""[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura""")
eu = int(input('Selecione a opção: '))
print('\033[1:31:40mJO\033[m')
sleep(1)
print('\033[1:33:40mKEN\33[m')
sleep(1)
print('\033[1:35:40mPÔ!!!\033[m')
sleep(0.5)
print('*~' * 12)
print(f'Computador jogou {itens[pc]}')
print(f'Jogador jogou {itens[eu]}')
print('*~' * 12)
if pc == 0: #PC jogou PEDRA
    if eu == 0:
        print('\033[1:30:43mEMPATE\033[m')
    elif eu == 1:
        print('\033[1:30:42mJOGADOR VENCE\033[m')
    elif eu == 2:
        print('\033[1:30:41mCOMPUTADOR VENCE\033[m')
    else:
        print('\033[1:31:40mJOGADA INVÁLIDA\033[m')
elif pc == 1: #PC jogou PAPEL
    if eu == 0:
        print('\033[1:30:41mCOMPUTADOR VENCE\033[m')
    elif eu == 1:
        print('\033[1:30:43mEMPATE\033[m')
    elif eu == 2:
        print('\033[1:30:42mJOGADOR VENCE\033[m')
    else:
        print('\033[1:31:40mJOGADA INVÁLIDA\033[m')
elif pc == 2: #PC jogou TESOURA
    if eu == 0:
        print('\033[1:30:42mO JOGADOR VENCE\033[m')
    elif eu == 1:
        print('\033[1:30:41mCOMPUTADOR VENCE\033[m')
    elif eu == 2:
        print('\033[1:30:43mEMPATE\033[m')
    else:
        print('\033[1:31:40mJOGADA INVÁLIDA\033[m')
