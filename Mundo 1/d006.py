enunciado ='''
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''

n = int(input('Digite um valor: '))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)
print(f'O valor digitado foi {n}; O dobro foi {dobro}, ', end=' ')
print(f'o triplo é {triplo} e sua raiz quadrada é {raiz}')
