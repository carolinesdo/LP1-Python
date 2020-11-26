# IDADE DOS HOMENS
h1 = int(input('Digite a idade do primeiro homem: '))
h2 =  int(input('Digite a idade do segundo homem: '))

# IDADE DAS MULHERES
m1 = int(input('Digite a idade da primeira mulher: '))
m2 = int(input('Digite a idade da segunda mulher: '))

#  ARRUMANDO A IDADE DOS HOMENS
if h1 > h2:
    hvelho = h1
    hnovo = h2
else:
    hvelho = h2
    hnovo = h1

# ARRUMANDO A IDADE DAS MULHERES
if m1 > m2:
    mvelha = m1
    mnova = m2
else:
    mvelha = m2
    mnova = m1

# SAIDA DAS IDADES ORGANIZADAS
print('Idade do homem mais velho: {}'.format(hvelho))
print('Idade do homem mais novo: {}'.format(hnovo))
print('Idade da mulher mais velha: {}'.format(mvelha))
print('Idade da mulher mais nova: {}'.format(mnova))

# REALIZANDO AS OPERAÇÕES SOLICITADAS
soma = hvelho + mnova
produto = hnovo * mvelha

# SAÍDA DAS OPERAÇÕES SOLICITADAS
print('A soma das idades do homem mais velho e da mulher mais nova vale: {}'.format(soma))
print('A multiplicação das idades do homem mais novo e da mulher mais velha vale: {}'.format(produto))
