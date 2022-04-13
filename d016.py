import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
arredondar = math.ceil(raiz)

print(f'A raiz de {num} é {raiz:.2f}, arrendodando para: {arredondar} !')
