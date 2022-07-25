from time import sleep
print('\33[1:33:40m =-=\033[m' * 20)
print('\33[1:33:40m SISTEMA BANCÁRIO\033[m')
print('\33[1:33:40m =-=\033[m' * 20)

imovel = float(input('Digite o valor do imóvel: '))
salario = float(input('Digite o valor do salário: '))
ano = float(input('Em quantos meses deseja pagar o imóvel?'))
em = imovel / ano
print('PROCESSANDO...')
sleep(2)
if em > salario * 0.3:
    print(f'\33[1:30:41m Infelizmente\33[m seu emprestimo não foi aprovado!')
else:
    print(f'\33[1:30:42m Parabés!\033[m Seu emprestimo de R$ {imovel:.2f} foi aprovado, e terá parcelas de R$ {em:.2f}!')
