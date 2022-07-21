enunciado ='''
Faça um programa que leia o ano de nascimento de 
um jovem e informe, de acordo com a sua idade, se ele ainda 
vai se alistar ao serviço militar, se é a hora exata de se 
alistar ou se já passou do tempo do alistamento. Seu programa 
também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date

ano = int(input('Digite seu ano de nascimento: '))

hoje = date.today().year

idade = hoje - ano

tempo = 18 - idade
maior = idade - 18
em = tempo + hoje
ema = hoje - maior
print(idade)

if idade == 18:
    print(f'Você nasceu no ano de {ano}, tem {idade} em {hoje}')
    print('Já é hora do alistamento militar!')
elif idade < 18:
    print(f'Você nasceu no ano de {ano}, tem {idade} em {hoje}')
    print(f'Ainda falta {tempo} anos para seu alistamento.')
    print(f'Seu alistamento será em {em}.')
elif idade > 18:
    print(f'Você nasceu no ano de {ano}, tem {idade} em {hoje}')
    print(f'Já passou {maior} anos do seu alistamento.')
    print(f'Seu alistamento foi em {ema}')
