print('Quadrado de um número')
num1 = int(input('Digite um número: '))
resp1 = num1 ** 2
print('O número digitado é {} e o seu valor ao quadrado vale {}'.format(num1, resp1))


print('Divisão entre dois números')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
div = n1 / n2
print('A divisão entre {} e {} vale {:.3f}'.format(n1, n2, div)) #DIV SERÁ APRESENTADA COM 3 CASAS DECIMAIS

print('Resto da divisão de um número por 2')
num2 = int(input('Digite um número: '))
div2 = num2 % 2
print('O resto da divisão de {} por 2 vale: {}'.format(num2, div2))

print('Média aritmética entre dois números')
n3 = float(input('Digite o primeiro número: '))
n4 = float(input('Digite o segundo número: '))
media = (n3 + n4) / 2
print('A média entre {:.1f} e {:.1f} vale {:.2f}'.format(n3, n4, media))

print('Cálculo da área, comprimento e diâmetro de uma circunferência')
raio = float(input('Digite o raio da circunferência: '))
pi = 3.14
area = pi * (raio ** 2)
comprimento = 2 * pi * raio
diametro = 2 * raio
print('Para uma circunferência de raio {} temos: área = {:.2f}, comprimento = {:.2f} e diâmetro = {:.2f}'. format(raio, area, comprimento, diametro))