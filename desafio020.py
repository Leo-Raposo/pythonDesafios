from random import shuffle

a1 = input('1º Aluno a apresentar: ')
a2 = input('2º Aluno a apresentar: ')
a3 = input('3º Aluno a apresentar: ')
a4 = input('4º Aluno a apresentar: ')
lista = [a1, a2, a3, a4]
shuffle(lista)

print(f'A Ordem dos alunos a apresentar será:\n {lista}')
