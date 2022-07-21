enunciado = '''
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
'''

pessoas = homem = mulheres = 0
while True:
    print('-' * 20)
    print('Cadastre uma pessoa')
    print('-' * 20)
    
    idade = int(input('Idade: '))
    
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    
    print('-' * 20)
    
    if idade > 18:
        pessoas += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if sexo == 'M':
        homem += 1

    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0 ]
    
    if continuar == 'N':
        break

print('======FIM DO PROGRAMA======')
print(f'Total de pessoas com mais de 18 anos: {pessoas}')
print(f'Ao todo, temos {homem} homens cadastrados.')
print(f'E temos {mulheres} mulheres com menos de 20 anos.')
