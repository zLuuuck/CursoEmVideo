enunciado ='''
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e 
qual foi o maior e o menor valores lidos. O programa deve perguntar
ao usuário se ele quer ou não continuar a digitar valores.
'''
resp = 's'
soma = quant = média = 0

while resp in 'Ss':
    núm = int(input('Digite um número: '))
    
    soma += núm
    quant += 1
    
    resp = str(input('Quer continuar? [s/n] ')).lower().strip()[0]
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor :
            menor = núm
média = soma / quant

print(f'Você digitou {quant} números e a média entre eles foi {média}')
