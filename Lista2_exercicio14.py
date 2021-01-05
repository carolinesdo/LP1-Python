'''
Faça um programa para calcular a soma, a subtração e a multiplicação de matrizes. 
Você pode fornecer a matriz no código, em vez de ler o que o usuário digitar, 
mas suas funções que fazem os cálculos devem ser úteis para qualquer tamanho de matriz 
desde que as propriedades matemáticas sejam respeitadas.
'''
print() # acrescenta uma linha vazia

# DADOS DAS MATRIZES
a = [[8,9,1],[5,6,5],[4,4,4]] 
b =  [[1,2,1],[3,4,1],[2,5,7]]
print('Matriz A: ', a)
print('Matriz B: ', b)
print() # acrescenta uma linha vazia

# SOMA DE MATRIZES
def somar(a, b):
    matriz_soma = []
    # Supondo que as duas matrizes possuem o mesmo tamanho
    quant_linhas = len(a) # Conta quantas linhas existem
    quant_colunas = len(a[0]) # Conta quantos elementos têm em uma linha
    for i in range(quant_linhas):
        # Cria uma nova linha na matriz_soma
        matriz_soma.append([])
        for j in range(quant_colunas):
            # Somando os elementos que possuem o mesmo índice
            soma = a[i][j] + b[i][j]
            matriz_soma[i].append(soma)
    return matriz_soma
print('Matriz Soma (A+B): ', somar(a,b))
print() # acrescenta uma linha vazia


# SUBTRAÇÃO DE MATRIZES
def subtrair(a, b):
    matriz_subtracao = []
    # Supondo que as duas matrizes possuem o mesmo tamanho
    quant_linhas = len(a) # Conta quantas linhas existem
    quant_colunas = len(a[0]) # Conta quantos elementos têm em uma linha
    for i in range(quant_linhas):
        # Cria uma nova linha na matriz_soma
        matriz_subtracao.append([])
        for j in range(quant_colunas):
            # Somando os elementos que possuem o mesmo índice
            subtracao = a[i][j] + b[i][j]
            matriz_subtracao[i].append(subtracao)
    return matriz_subtracao
print('Matriz Subtração (A-B): ', subtrair(a,b))
print() # acrescenta uma linha vazia

# MULTIPLICAÇÃO DE MATRIZES
def linhaColuna(a,b):
  if (len(a) >= len(b)):
    return a,b
  return b,a

def testaSePossiveMultiplicarMatrizes(a,b):
  retorno = False
  if (len(a) == len(b[0])):
    retorno = True
  
  return retorno

def multiplicaMatrizes(a,b):

  r = []

  for i in range(len(a)):
    linhaAux = []
    for j in range(len(b[0])):      
      aux = 0
      for w in range(len(b)):
        aux += a[i][w]*b[w][j]
      linhaAux.append(aux)
    r.append(linhaAux)

  return r


if testaSePossiveMultiplicarMatrizes(a,b):
  print('Matriz Multiplicação (A*B): ',multiplicaMatrizes(a,b))
else:
  print("não é possível multiplicar as matrizes")