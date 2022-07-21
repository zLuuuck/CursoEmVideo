enunciado = '''
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
no final, mostre:
A) Qual é o total gasto na compra
B) Quantos produtos custam mais de R$1000
c) Qual é o nome do produto mais barato
'''
total = produto = menor = cont = 0
nomeMenor = ''

print('-' * 20)
print(' ' * 5 + 'LOJA SUPER BARATÃO')
print('-' * 20)
while True:
    nome = str(input('Nome do Produto: ')).strip()
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço >= 1000.00: produto += 1

    if cont == 1 or preço < menor:
        menor = preço
        nomeMenor = nome
    
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
     
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    
    if continuar == 'N':
        break
print('-' * 5 + 'FIM DO PROGRAMA' + '-' * 5)
print(f'O total da compra foi de R${total:.2f}')
print(f'Temos {produto} custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeMenor} que custa R${menor:.2f}')