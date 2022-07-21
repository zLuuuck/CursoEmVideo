enunciado ='''
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la, 
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
'''

a = float(input('Digite a altura da sua parede em metros: '))
la = float(input('Digite a largura da sua parede em metros: '))

area = a * la
tinta = area / 2

print(f'Largura: {la}, altura: {a}. Area de {area}m².')
print(f'Será gasto no mínimo {tinta}L de tinta.')
