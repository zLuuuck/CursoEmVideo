enunciado ='''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, 
de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida
'''
import math

peso = float(input('Qual seu peso em Kg? '))
altura = float(input('Qual sua altura em metros( use . )? '))

alt = math.pow(altura, 2)
imc = peso / alt
if imc < 18.5:
    print(f'O seu IMC é de {imc:.2f};')
    print('Você esta ABAIXO do normal, magreza.')
elif imc < 24.9:
    print(f'O seu IMC é de {imc:.2f};')
    print('Você está no peso correto.')
elif imc < 29.9:
    print(f'O seu IMC é de {imc:.2f};')
    print('Você esta ACIMA do peso, sobrepeso.')
elif imc < 39.9:
    print(f'O seu IMC é de {imc:.2f};')
    print('Você está MUITO ACIMA do peso, OBESIDADE.')
elif imc > 40.0:
    print(f'O seu IMC é de {imc:.2f};')
    print('Você esta EXTREMAMENTE ACIMA do peso, OBESIDADE EXTREMA.')
    print('CUIDADO!!')
