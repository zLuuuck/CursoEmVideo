d = int(input('Quantos dias alugado? '))
km = float(input('Quantos Km rodados? '))
vpd = d * 60
vpkm = km * 0.15
s = vpd + vpkm

print(f'Dias usados: {d}, preço por dia: R$60')
print(f'Total do preço por dia: {vpd}')
print(f'Km rodados: {km}, preço por km: 0,15')
print(f'Total do preço por dia: {vpkm}')
print(f'O valor total a pagar é de {s},')
