nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
primeiro = n[0]
ultimo = n[-1]
print(f'Seu primeiro nome é: {primeiro}')
print(f'Seu ultimo nome é {ultimo}')
