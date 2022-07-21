enunciado ='''
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
'''

cidade = str(input('Digite o nome da cidade: ')).strip()

Aprovação = cidade[:5].upper() == 'SANTO'

print(f'Cidade digitada: {cidade}')
print(f'Começa com "Santo"? {Aprovação}')
