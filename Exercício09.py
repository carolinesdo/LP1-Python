n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 == n2:
    print('Os números digitados são iguais!')
elif n1 > n2:
    print('{} é o maior dos valores digitados'.format(n1))
else:
    print('{} é o maior dos valores digitados'.format(n2))