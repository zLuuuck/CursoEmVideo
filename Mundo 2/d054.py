enunciado ='''
Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade 
e quantas já são maiores.
'''
import os
os.system('cls')
from datetime import date
hoje = date.today().year
pessoas = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = hoje - ano
    if idade == 21:
        pessoas = pessoas + 1
    elif idade > 21:
        pessoas = pessoas + 1
    elif idade < 21:
        pessoas = pessoas + 0
    menor = 7 - pessoas
print('=-' * 30)
print(f'{pessoas} pessoas já são maiores de idade!')
print(f'{menor} pessoas ainda são menores de idade!')