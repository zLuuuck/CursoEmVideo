enunciado ='''
Refaça o DESAFIO 35 dos triângulos, acrescentando o 
recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes
'''
txt = '''
─░▄█▀▄─▒██▄░▒█▌─░▄█▀▄─▒██░░░░▐██▒▄█▀▀█─░▄█▀▄─░▐█▀█▄▒▐█▀▀█▌▒▐█▀▀▄
░▐█▄▄▐█▒▐█▒█▒█░░▐█▄▄▐█▒██░░░─░█▌▒▀▀█▄▄░▐█▄▄▐█░▐█▌▐█▒▐█▄▒█▌▒▐█▒▐█
░▐█─░▐█▒██░▒██▌░▐█─░▐█▒██▄▄█░▐██▒█▄▄█▀░▐█─░▐█░▐█▄█▀▒▐██▄█▌▒▐█▀▄▄
                        ░▐█▀█▄░▐█▀▀
                        ░▐█▌▐█░▐█▀▀
                        ░▐█▄█▀░▐█▄▄
▒█▀█▀█▒▐█▀▀▄░▐██─░▄█▀▄─▒██▄░▒█▌░▐█▀▀▀─▒█▒█▒██░░░▒▐█▀▀█▌▒▄█▀▀█
░░▒█░░▒▐█▒▐█─░█▌░▐█▄▄▐█▒▐█▒█▒█░░▐█░▀█▌▒█▒█▒██░░░▒▐█▄▒█▌▒▀▀█▄▄
░▒▄█▄░▒▐█▀▄▄░▐██░▐█─░▐█▒██░▒██▌░▐██▄█▌▒▀▄▀▒██▄▄█▒▐██▄█▌▒█▄▄█▀
'''
print(txt)

r1 = float(input('Digite o 1° segmento: '))
r2 = float(input('Digite o 2° segmento: '))
r3 = float(input('Digite o 3° segmento: '))

if r1 == r2 == r3:
    print('Os 3 segmentos acima PODEM formar um triângulo Equilátero.')
elif r1 == r2 or r2 == r3 or r3 == r1:
    print('Os 3 segmentos acima PODEM formar um triângulo Isósceles.')
elif r1 != r2 != r3 and r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('Os 3 segmentos acima PODEM formar um triângulo Escaleno.')
else:
    print('não é um triângulo')
