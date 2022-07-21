enunciado ='''
Elabore um programa que calcule o valor a ser pago 
por um produto, considerando o seu preço normal e 
condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros
'''

print('=============Loja Do zLuuuck=============')
preço = float(input('Digite o Preço das compras: '))
txt = """
FORMAS DE PAGAMENTO:
[1] A vista com dinheiro/cheque
[2] A vista no cartão.
[3] Em até 2x no cartão.
[4] 3x ou mais no cartão.

"""
print(txt)
opção = input(': ')

if opção == '1':
    desconto = (preço * 10) / 100
    total = preço - desconto
    print('FORMA DE PAGAMENTO ESCOLHIDA: ')
    print('A vista no dinheiro/cheque.')
    print(f'Sua compra de R${preço} vai custar R${total} no final.')
elif opção == '2':
    desconto = (preço * 5) / 100
    total = preço - desconto
    print('FORMA DE PAGAMENTO ESCOLHIDA: ')
    print('A vista no cartão.')
    print(f'Sua compra de R${preço} vai custar R${total} no final.')
elif opção == '3':
    total = preço
    parcela = total / 2
    print(f'Sua compra sera parcelada em 2x de R${parcela:.2f}')
    print(f'Sua compra de R${preço} vai custar R${total} no final.')
elif opção == '4':
    total = preço + ((preço * 20) / 100)
    totalParcelas = int(input('Quantas parcelas? '))
    parcela = total / totalParcelas
    print(f'Sua conta será parcelada em {totalParcelas}x de R${parcela:.2f} COM JUROS')
    print(f'Sua compra de R${preço} vai custar R${total} no final.')
