'''
Faça um programa para multiplicar matrizes 3x3.
'''
a = [[1,5,2],[2,4,6],[7,1,3]]
b = [[1,4,7],[5,1,0],[3,1,1]]

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
  print(multiplicaMatrizes(a,b))
else:
  print("não é possível multiplicar as matrizes")
