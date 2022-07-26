from random import randint
from time import sleep
print('VAMOS JOGAR JOKENPÔ? FAÇA SUA ESCOLHA!!!')
print("""[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura""")
eu = int(input('Selecione a opção: '))
pc = randint(1, 3)
print('PROCESSANDO...')
sleep(1)
if eu == 1 and pc == 2:
    print('Você escolheu PEDRA e eu PAPEL. Eu ganhei!')
elif eu == 1 and pc == 3:
    print('Você escolheu PEDRA e eu TESOURA!. Parabéns, você ganhou!')
elif eu == 2 and pc == 1:
    print('Você escolheu PAPEL e eu PEDRA! Parabéns, você ganhou!')
elif eu == 2 and pc == 3:
    print('Você escolheu PAPEL e eu TESOURA! Eu ganhei!')
elif eu == 3 and pc == 1:
    print('Você escolheu TESOURA e eu PEDRA! Eu ganhei!')
elif eu == 3 and pc == 2:
    print('Você escolheu TESOURA e eu PAPEL! Parabéns, você ganhou!')
elif eu > 3:
    print('Número não encontrado! Escolha um número acima!')
else:
    print('Deu empate!')
