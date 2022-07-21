enunciado ='''
A Confederação Nacional de Natação precisa de um programa 
que leia o ano de nascimento de um atleta e mostre sua 
categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER
'''
from datetime import date

ano = int(input('Digite seu ano de nascimento: '))

hoje = date.today().year

idade = hoje - ano

if idade <= 9:
    print(f'Você tem {idade}.')
    print('classificação: Mirim')
elif idade <= 14:
    print(f'Você tem {idade}.')
    print('classificação: Infantil')
elif idade <= 19:
    print(f'Você tem {idade}.')
    print('classificação: Junior')
elif idade <= 25:
    print(f'Você tem {idade}.')
    print('classificação: Sênior')
elif idade > 25:
    print(f'Você tem {idade}.')
    print('classificação: Master')
