enunciado = '''
Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''

n = int(input('Qual o valor a ser sacado? R$'))

c50 = n//50
c20 = (n % 50)//20
c10 = ((n % 50) % 20)//10
c5 = (((n % 50) % 20) % 10)//5
c = (((n % 50) % 20) % 10) % 5
if c50 != 0:
    print(f'Total de {c50} cédulas de R$50')
if c20 != 0:
    print(f'Total de {c20} cédulas de R$20')
if c10 != 0:
    print(f'Total de {c10} cédulas de R$10')
if c5 != 0:
    print(f'Total de {c5} cédulas de R$5')
if c != 0:
    print(f'Total de {c} cédulas de R$1')