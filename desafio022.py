import re
nome = input('Digite seu nome completo: ')

nup = nome.upper()
nlo = nome.lower()
ns = len(re.sub(r"\s+", "", nome))
sc = len(nome.split()[0])

print(f"""Nome com letras maiúsculas: {nup}
Nome com letras minúsculas: {nlo}
Quantas letras ao todo: {ns}
Quantas letras tem o primeiro nome: {sc}""")
