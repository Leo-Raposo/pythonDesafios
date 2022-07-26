print('º-º' * 10)
print('Calculadora de IMC')
print('º-º' * 10)

p = float(input('Digite seu peso: '))
a = float(input('Digite sua altura: '))

imc = p / (a * a)

if imc < 18.5:
    print(f'Seu IMC é {imc:.2F}, ABAIXO DO PESO!')
elif imc <= 25:
    print(f'Seu IMC é {imc:.2F}, PESO IDEAL!')
elif imc <= 30:
    print(f'Seu IMC é {imc:.2F}, SOBREPESO!')
elif imc <=40:
    print(f'Seu IMC é {imc:.2F}, OBESIDADE!')
elif imc >= 40:
    print(f'Seu IMC é {imc:.2F}, OBESIDADE MÓRBIDA!')
