enunciado ='''
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''

metro = float(input('Digite uma distância em metros: '))
dm = metro * 10
cm = metro * 100
mm = metro * 1000
dam = metro / 10
hm = metro / 100
km = metro / 1000
print(f'A medida de {metro}m corresponde a \n{km}km \n{hm}hm \n', end='')
print(f'{dam}dam \n{dm}dm \n{cm}cm \n{mm}mm')
