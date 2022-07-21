enunciado ='''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
'''

real = float(input('Digite quanto você tem na carteira: R$'))
dólar = real / 3.27
print(f'Você tem R${real:.2f}, convertendo, você tem US${dólar:.2f}!')
