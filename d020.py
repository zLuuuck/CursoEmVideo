import random

a1 = str(input('Primerio aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
ordem = random.sample(lista, len(lista))
print(f'a ordem é: {ordem} !')
