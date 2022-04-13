a = float(input('Digite a altura da sua parede em metros: '))
la = float(input('Digite a largura da sua parede em metros: '))

area = a * la
tinta = area / 2

print(f'Largura: {la}, altura: {a}. Area de {area}m².')
print(f'Será gasto no minimo {tinta}L de tinta.')
