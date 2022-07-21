enunciado ='''
Desenvolva um programa que leia seis números inteiros e
mostre a soma apenas daqueles que forem pares. Se o valor 
digitado for ímpar, desconsidere-o.
'''
soma = 0
cont = 0
for c in range(1, 7):
    nu = int(input('Digite um número: '))
    if nu % 2 == 0:
        soma += nu
        cont += 1
if cont == 0:
    print('=-' * 10)
    print('Não foi digitado nenhum valor PAR.')
else:
    print('=-' * 10)
    print(f'Foi digitado {cont} números pares.')
    print(f'A soma dos valores PARES digitados foi de {soma}.')
