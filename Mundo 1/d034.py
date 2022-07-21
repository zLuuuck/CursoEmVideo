enunciado ='''
Escreva um programa que pergunte o salário 
de um funcionário e calcule o valor do seu 
aumento. Para salários superiores a R$1250,00, 
calcule um aumento de 10%. Para os inferiores 
ou iguais, o aumento é de 15%.
'''

sal = float(input('Digite o seu salário(use com "." invés de ","): R$'))


def aumento10():
    novo = sal + (sal * 10 / 100)
    print(f'Seu salário que antes era de {sal:.2f}, agora é de {novo:.2f}')


def aumento15():
    novo = sal + (sal * 15 / 100)
    print(f'Seu salário que antes era de {sal:.2f}, agora é de {novo:.2f}')


if sal > 1250.00:
    aumento10()
else:
    aumento15()
