enunciado ='''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
nu = int(input('Digite um número: '))
total = 0
for c in range(1, nu + 1):
    if nu % c == 0:
        print('\033[033m', end=' ')
        total += 1
    else:
        print('\033[031m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[m0 número {nu} foi divisível {total} vezes.')
if total == 2:
    print('Esse número é primo')
else:
    print('Esse número não é primo')
