enunciado ='''
Escreva um programa em Python que leia um número inteiro 
qualquer e peça para o usuário escolher qual será a base 
de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
'''

txt = """
░▐█▀█▒▐█▀▀█▌▒██▄░▒█▌▒▐▌▒▐▌░▐█▀▀▒▐█▀▀▄▒▄█▀▀█─░▄█▀▄─▒▐█▀▀█▌
░▐█──▒▐█▄▒█▌▒▐█▒█▒█░░▒█▒█░░▐█▀▀▒▐█▒▐█▒▀▀█▄▄░▐█▄▄▐█▒▐█▄▒█▌
░▐█▄█▒▐██▄█▌▒██░▒██▌░▒▀▄▀░░▐█▄▄▒▐█▀▄▄▒█▄▄█▀░▐█─░▐█▒▐██▄█▌

"""
txt2 = """
    [ 1 ] Binário
    [ 2 ] Octal
    [ 3 ] Hexadecimal

"""
print(txt)
num = int(input('Digite um número inteiro: '))
print(txt2)
opção = int(input('Sua opção: '))

if opção == 1:
    print('{} convertido pra binario, fica {}'.format(num, bin(num)))
elif opção == 2:
    print('{} convertido pra octal, fica {}'.format(num, oct(num)))
elif opção == 3:
    print('{} convertido pra hexadecimal, fica {}'.format(num, hex(num)))
