enunciado ='''
Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.
'''

nome = str(input('Digite seu nome: ')).strip()
alto = nome.upper()
baixo = nome.lower()
total = len(nome) - nome.count(' ')
separa = nome.split()
nome1 = separa[0]
primeiro = len(separa[0])
print('Analisando o nome . . .')
print(f'Seu nome em maiúsculas: {alto}')
print(f'Seu nome em minúsculas: {baixo}')
print(f'Seu nome ao todo tem {total} letras')
print(f'Seu primeiro nome é {nome1} tem {primeiro} letras')
