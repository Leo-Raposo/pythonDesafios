print('=-=' * 20)
print('Analisador de Triângulos')
print('=-=' * 20)
r1 = float(input('Digite o comprimeto da reta 1: '))
r2 = float(input('Digite o comprimeito da reta 2: '))
r3 = float(input('Digite o comprimeito da reta 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR um triângulo!')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR um triângulo')
