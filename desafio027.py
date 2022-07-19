nome = str(input('Digite seu nome completo: ')).strip()
a1 = nome.split()
print(f'Muito prazer em te conhecer {nome}!')
print(f"""Seu Primeiro nome é: {a1[0]}
Seu último nome é: {a1[-1]}""")
