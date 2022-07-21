enunciado ='''
Escreva um programa que faça o computador “pensar” 
em um número inteiro entre 0 e 5 e peça para o usuário 
tentar descobrir qual foi o número escolhido pelo 
computador. O programa deverá escrever na tela se 
o usuário venceu ou perdeu.
'''

import random
computador = random.randint(0, 5)
jogador = int(input('Pense em um número de 1 a 5: '))
if computador == jogador:
    print(f'Você ganhou! eu pensei no {computador}')
else:
    print(f'Você perdeu! eu pensei no {computador}')
