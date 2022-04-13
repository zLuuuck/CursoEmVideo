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
