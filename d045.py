import random
import time

itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)
# print(f'o computador escolheu {itens[computador]}')
print("""Pedra, Papel e Tesoura
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[0] Pedra
[1] Papel
[2] Tesoura
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
""")
jogador = int(input('Qual é a sua jogada? '))

time.sleep(1)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!')
time.sleep(1)
print('-=' * 10)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 10)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador VENCE')
    elif jogador == 2:
        print('Computador VENCE')

elif computador == 1:
    if jogador == 0:
        print('Computador VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador VENCE')

elif computador == 2:
    if jogador == 0:
        print('Jogador VENCE')
    elif jogador == 1:
        print('Computador Vence')
    elif jogador == 2:
        print('EMPATE')
