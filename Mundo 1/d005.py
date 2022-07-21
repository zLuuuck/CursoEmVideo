enunciado ='''
Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
'''

n = int(input('Digite um número: '))
Sucessor = n + 1
Antecessor = n - 1

print(f'O valor digitado foi: {n}; Seu Sucessor é {Sucessor};', end=' ')
print(f'E seu antecessor é {Antecessor}')
