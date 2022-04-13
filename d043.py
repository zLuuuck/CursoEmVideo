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
