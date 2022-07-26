n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2) / 2

if m < 5.0:
    print(f'Sua média é {m}. \033[1:30:41mREPROVADO!!!\033[m')
elif m <= 6.9:
    print(f'Sua média é {m}, Você está de \033[1:30:43mRECUPERAÇÃO!!!\033[m')
#elif m >= 7.0:
else:
    print(f'Sua média é {m}, Parabés, você foi \033[1:30:42mAPROVADO!!!\033[m')