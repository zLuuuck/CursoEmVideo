frase = str(input('Digite uma frase: ')).lower().strip()
contando = frase.count('a')
A1 = frase.find('a')+1
A2 = frase.rfind('a')+1
print(f'A letra "A" aprece {contando} vezes')
print(f'A primeira letra "A" aparece na posição {A1}')
print(f'A ultima letra "A" aparece na posição {A2}')
