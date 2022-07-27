t1 = int(input('Digite quantos termos: '))
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
n1 = t + (t1 - 1) * r
for pa in range(t, n1 + r, r):
    print(f'{pa}', end=' \U0001F812 ')
print('ACABOU')
