enunciado ='''
Faça um programa que leia o peso de cinco pessoas. 
No final, mostre qual foi o maior e o menor peso lidos
'''
import os
os.system('cls')
maior = 0
menor = 0
for p in range(1, 6):
    peso = float((input(f'Peso da {p}ª pessoa: ')))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('=-' * 20)
print(f'O maior peso lido foi {maior}Kg')
print(f'O menor peso lido foi {menor}Kg')