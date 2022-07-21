enunciado ='''
Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
'''

nome = str(input('Digite o seu nome: ')).strip()

Aprovação = 'silva' in nome.lower()

print(f'Nome digitado: {nome}')
print(f'Tem "Silva"? {Aprovação}')
