soma = 0
cont = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'Foram encontrados {cont} números múltiplos de 3 ímpares ')
print(f'A soma de todos os múltiplos de 3 ÍMPARES é {soma} ') 

