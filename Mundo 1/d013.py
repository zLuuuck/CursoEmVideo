enunciado ='''
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''

sal = float(input('Digite o seu salário(use com "." invés de ","): R$'))
aumento = float(input('Digite a % do aumento: '))
novo = sal + (sal * aumento / 100)
totalau = sal - novo

print(f'Seu salário é de R${sal:.2f}. Você ganhou {aumento}% de aumento,', end=' ')
print(f'agora ele é de R${novo:.2f}')
print(f'Ganhou-se R${totalau:.2f}')
