'''
Escreva um programa para ler valores inteiros fornecidos pelo usuário e escrevê-los em ordem crescente.
'''

print('Ordenar os números digitados pelo usuário em ordem crescente.')
print('Digitar todos os números com a mesma quantidade de caracteres. EX: 01,98, 17, 65, 07 ...')
vetor = []
num = " "
while (num != '.'):
  num = input('Digite um número ou . para encerrar: ') 
  if num != ".":
    vetor.append(num)
vetor.sort()
print(vetor)