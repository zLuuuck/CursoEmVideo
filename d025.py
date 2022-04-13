nome = str(input('Digite o seu nome: ')).strip()

Aprovação = 'silva' in nome.lower()

print(f'Nome digitado: {nome}')
print(f'Tem "Silva"? {Aprovação}')
