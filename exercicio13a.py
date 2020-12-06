'''
script para ler duas matrizes de qualquer tamanho com entradas fornecidas pelo usuário.
'''
print("Dados da matriz A")
la = int(input('Digite o número de linhas da matriz A: '))
ca = int(input('Digite o número de colunas da matriz A: '))
a = [[],[],[]]  # MATRIZ A
for l in range(0,la):
    for c in range(0,ca):
        a[l].append(int(input(f"Digite um valor para [{l},{c}]: ")))

print('-='*30) # unidade de separação entre as matrizes


print('Dados da matriz B')
lb = int(input('Digite o número de linhas da matriz B: '))
cb = int(input('Digite o número de colunas da matriz B: '))
b = [[],[],[]] #$ MATRIZ 2 OU MATRIZ B
for l in range(0,lb):
    for c in range(0,cb):
        b[l].append(int(input(f"Digite um valor para [{l},{c}]: ")))

print('-='*30) # unidade de separação entre as matrizes

# print das matrizes digitadas

print(' ')
print('Matriz A')
for l in range(0,la):
    for c in range(0,ca):
        print(f'{a[l][c]:^8}', end='')
    print() # FAZ PULAR A LINHA

print('-='*30)
print('Matriz B')
for l in range(0,lb):
    for c in range(0,cb):
        print(f'{b[l][c]:^8}', end='')
    print() # FAZ PULAR A LINHA

print('-='*30)