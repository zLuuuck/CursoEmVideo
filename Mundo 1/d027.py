enunciado ='''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
'''

nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
primeiro = n[0]
ultimo = n[-1]
print(f'Seu primeiro nome é: {primeiro}')
print(f'Seu ultimo nome é {ultimo}')
