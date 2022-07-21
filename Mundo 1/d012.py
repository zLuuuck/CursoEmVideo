enunciado ='''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''

preço = float(input('Digite o preço do produto: R$'))
des = float(input('Digite o a porcentagem do desconto: '))
novo = preço - (preço * des / 100)
totaldes = preço - novo

print(f'O preço é R${preço:.2f}, com um desconto de {des}%, fica R${novo:.2f}.')
print(f'O desconto é de R${totaldes:.2f}')
