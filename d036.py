vcasa = int(input('Digite o Valor da Casa: '))
sal = int(input('Digite o Valor do seu Salário: '))
anos = int(input('Digite em quantos anos você vai pagar: '))

# 200k, 1k, 50 anos
parcela = vcasa / (anos * 12)
messes = anos * 12
novo = (sal * 30) / 100

if novo < parcela:
    print('Você infelizmente não pode fazer o empréstimo.')
else:
    print(f'Você irá parcelar em {messes}, pagando R${parcela} por parcela.')
