enunciado = '''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo
'''

while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 20)
    if num < 0:
        break
    for c in range(1, 11):
        multiplicação = num * c
        print(f'{num} x {c} = {multiplicação}')
    print('-' * 20)

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')