print('\033[1:34:40m~*~\33[m' * 20)
print('Bem Vindo a Confederação Nacional de Natação!')
print('\033[1:34:40m~*~\033[m' * 20)
n = int(input('Insira o seu ano de nascimento: '))

a = 2022 - n

if a <= 9:
    print(f'Você tem {a} anos, a sua categoria será a \033[1:32:40mMIRIM!\033[m')
elif a <= 14:
    print(f'Você tem {a} anos, a sua categoria será a \033[1:33:40mINFANTIL!\033[m')
elif a <= 19:
    print(f'Você tem {a} anos, a sua categoria será a \033[1:34:40mSÊNIOR!\033[m')
elif a > 19:
    print(f'Você tem {a} anos, a sua categoria será a \033[1:35:40mMASTER!\033[m')
else:
    print('Ano incorreto, favor inserir novamente!')
