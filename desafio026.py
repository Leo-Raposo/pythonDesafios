frase = str(input('Digite uma frase: ')).strip().upper()

a = frase.count('A')
a2 = frase.find('A') + 1
a3 = frase.rfind('A') + 1

print(f"""A Letra A Aparece {a} vezes na frase.
A primeira letra A aparece na posição {a2}
A última letra A apareceu na posição {a3}""")
