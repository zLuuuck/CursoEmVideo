enunciado ='''
Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar 
mais alguns termos. O programa encerrará quando ele disser que quer 
mostrar 0 termos.
'''
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while c <= total:
        print(f'{p} => ', end='')
        p += r
        c += 1
    print('Pausa.')
    mais = int(input('Quantos termos a mais quer mostrar? '))
print(f'Progressão finalizada com {total} termos mostrados.')