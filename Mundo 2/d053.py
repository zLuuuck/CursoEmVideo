enunciado ='''
Crie um programa que leia uma frase qualquer e 
diga se ela é um palíndromo, desconsiderando os 
espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA.
'''

frase = str(input('Digite sua frase: ')).strip().upper()
separação = frase.split()
junto = ''.join(separação)
inverso = junto[::-1]
print('=-' * 30)
if inverso == junto:
    print('É um palíndromo')
else:
    print('não é um palíndromo')
print(f'A frase digitada foi {junto}.')
print(f'Ela ao contrário é {inverso}')
