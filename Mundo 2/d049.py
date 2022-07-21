enunciado ='''
Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
'''
nu = int(input('Digite um número: '))

for c in range(1, 101):
    multi = nu * c
    print(f'{c} x {nu} = {multi}')
