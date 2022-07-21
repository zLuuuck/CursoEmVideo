enunciado ='''
Desenvolva um programa que leia o primeiro termo e a razão de 
uma PA. No final, mostre os 10 primeiros termos dessa progressão.
'''
print('=-'*20)
print('10 termos de uma Progressão Aritmética')
print('=-'*20)


primeiro = int(input('Digite o primeiro termo: '))

r = int(input('Digite a razão: '))
décimo = primeiro + (1 - 1) * r
for c in range(primeiro, décimo + r, r):
    print(c, end=' => ')
    
print('Acabou!')