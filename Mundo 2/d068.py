enunciado = '''
Faça um programa que joguem par ou ímpar com o computador.
O jogo será interrompido quando o jogador PERDER, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo.
'''
import random
v = 0
while True:
    print('=-' * 20)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('=-' * 20)
    n = int(input('Digite um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    computador = random.randint(1, 11)
    resultado = computador + n
    validação = resultado % 2
    print(f'Você jogou {n} e o computador {computador}. Total de {resultado}.')
    if escolha == 'P':
        if resultado % 2 == 0: 
            print('Você venceu!')
            v += 1
        elif resultado % 2 == 1:
            break
    if escolha == 'I':
        if resultado % 2 == 1: 
            print('Você venceu!')
            v += 1
        elif resultado % 2 == 0:
            break
print('-' * 20)
print('você PERDEU!')
print('-' * 20)
print('GAME OVER')
print(f'Você venceu {v} vezes.')