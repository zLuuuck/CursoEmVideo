import random
computador = random.randint(0, 5)
jogador = int(input('Pense em um número de 1 a 5: '))
if computador == jogador:
    print(f'Você ganhou! eu pensei no {computador}')
else:
    print(f'Você perdeu! eu pensei no {computador}')
