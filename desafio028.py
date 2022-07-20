from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-' * 20)
pc = randint(0, 5) #comando para sortear número
j = int(input('Em que número eu pensei? '))
print('PROCESSANDO ...')
sleep(2)
if j == pc:
    print('PARABÉNS! Você conseguiu me vencer')
else:
    print(f'GANHEI! Eu pensei no número {pc} e não no {j}')
