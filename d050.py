soma = 0
for c in range(0, 7):
    nu = int(input('Digite um número: '))
    if nu % 2 == 0:
        soma = soma + nu
print(f'A soma dos valores PARES digitados foi de {soma}')
