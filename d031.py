dis = float(input('Qual é a distância da sua viajem? '))

if dis <= 200:
    preço = dis * 0.50
    print(f'A sua viagem de {dis} deu R${preço:.2f}! Tenha uma boa viajem.')
else:
    preço = dis * 0.45
    print(f'A sua viagem ultrapassou 200km ({dis})', end=' ')
    print(f'Temos um desconto! Você pagará apenas {preço:.2f}!')
