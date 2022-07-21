enunciado ='''
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números 
foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''
digitados = 0
soma = 0
nu = 0
while nu != 999:
    nu = int(input('Digite um número[999 para]: '))
    digitados += 1
    soma += nu
    if nu == 999:
        print(f'Foram digitados {digitados - 1} números! A soma entre eles resulta em {soma - 999}!')
        break
