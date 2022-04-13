vel = int(input('Qual a velocidade atual do carro? '))

if vel > 80:
    print('Você foi multado!')
    multa = (vel - 80) * 7
    print(f'Deverá pagar uma multa de R${multa:.2f}!')
else:
    print('Tenha um bom dia! Dirija com segurança!')
