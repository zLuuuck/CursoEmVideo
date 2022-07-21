enunciado ='''
Faça um programa que leia um ângulo qualquer e
mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''

import math

an = float(input('Digite o ângulo que você deseja:'))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))

print(f'Ângulo: {an} ')
print(f'Ângulo Seno: {seno:.2f} ')
print(f'Ângulo Cosseno: {cosseno:.2f} ')
print(f'Ângulo Tangente: {tangente:.2f} ')
