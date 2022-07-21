enunciado ='''

'''
soma = 0
idades = 0
nomevelho = ' '
totalm20 = 0

for p in range(1, 5):
    print(f'----- {p}ª Pessoa -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    soma += idade

    if p == 1 and sexo in 'Mm':
        idades = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > idades:
        idades = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalm20 += 1

média = soma / 4

print(f'A média de idade do grupo é de {média} anos.')
print(f'a maior idade é {idades} anos, seu nome é {nomevelho}')
print(f'ao todo são {totalm20} com menos de 20 anos')
