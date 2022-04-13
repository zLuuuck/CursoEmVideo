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
