enunciado ='''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('''
          [1] Soma
          [2] Multiplicação
          [3] Maior
          [4] Novos números
          [5] Sair do programa
          ''')
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}!')
    elif opção == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} x {n2} é {produto}!')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre os números {n1} e {n2} o maior valor é {maior}!')
    elif opção == 4:
        print('Informe seus números novamente.')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-' * 20)
print('Fim do programa, volte sempre!')
