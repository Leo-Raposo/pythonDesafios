d = float(input('Digite a distância da sua viagem: '))
t1 = d * 0.5
t2 = d * 0.45
if d <= 200:
    print(f'A distância é de {d:.2f}Km e custará R$ {t1:.2f}')
else:
    print(f'A distância é de {d:.2f}Km e custará R$ {t2:.2f}')
