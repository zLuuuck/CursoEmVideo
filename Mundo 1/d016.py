enunciado ='''
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
'''

import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
arredondar = math.ceil(raiz)

print(f'A raiz de {num} é {raiz:.2f}, arrendondando para: {arredondar} !')
