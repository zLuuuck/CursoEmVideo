enunciado ='''
Faça um programa que leia algo pelo teclado e mostre na tela
o seu tipo primitivo e todas as informações possíveis sobre ele.
'''

n = input('Digite algo:')

tipo = type(n)
an = n.isalnum()
a = n.isalpha()
nu = n.isnumeric()
espaco = n.isspace()
ma = n.isupper()
mi = n.islower()
cap = n.istitle()
print(f'O tipo primitivo primitivo deste valor é {type(n)}')
print(f'Só tem espaços? {espaco}')
print(f'É um número? {nu}')
print(f'É alfabético? {a}')
print(f'É alfanumero? {a}')
print(f'Está em maiúsculas? {ma}')
print(f'Está em minúsculas? {mi}')
print(f'Está capitalizada? {cap}')
