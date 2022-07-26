from time import sleep
print('\33[1:33:40m =-=\033[m' * 20)
print('\33[1:33:40m SISTEMA BANCÁRIO\033[m')
print('\33[1:33:40m =-=\033[m' * 20)

imovel = float(input('Digite o valor do imóvel: R$ '))
salario = float(input('Digite o valor do salário: R$ '))
ano = int(input('Em quantos anos deseja pagar o imóvel? '))
em = imovel / (ano * 12)
print('PROCESSANDO...')
sleep(1)
if em > salario * 0.3:
    print(f"""Seu emprestimo de R$ {imovel:.2f} em {ano} anos tem pestações de R$ {em:.2f}!
Emprestimo \33[1:30:41mNEGADO\33[m""")
else:
    print(f"""Seu emprestimo de R$ {imovel:.2f} em {ano} anos tem prestações de R$ {em:.2f}!
Emprestimo \33[1:30:42mAPROVADO!\033[m""")
