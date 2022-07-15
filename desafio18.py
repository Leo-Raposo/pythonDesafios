import math

a = int(input('Insira um angulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))

print(f'Você digitou {a:.2f}º\n o seu seno é {s:.3f}\n o seu cosceno é {c:.3f}\n a sua tangente é {t:.3f}')