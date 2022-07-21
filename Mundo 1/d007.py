enunciado ='''
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

print(f'A média do aluno foi de {media:.2f}')

if media < 7.0:
    print('Reprovado')
elif media > 7.0:
    print('Aprovado')

