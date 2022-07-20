from time import sleep

print('===' * 12)
print('Bem vindo ao sistema do DETRAN/DF')
print('===' * 12)
print()
vel = float(input('Insira a velocidade do veículo: '))
m = (vel - 80) * 7
print('PROCESSANDO...')
sleep(2)
print(f'O Radar captou o carro a {vel:.2f} Km/h')
if vel <= 80:
    print('A velocidade está dentro da permitida')
else:
    print(f'A velocidade permitida é de 80 Km/h. Sua multa é de R$ {m:.2f}')
