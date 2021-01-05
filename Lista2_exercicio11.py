'''
Crie um programa para ler uma string fornecida pelo usuário. Informe se essa string forma um palíndromo.
'''

palavra1 = str(input('Digite a palavra que você deseja verificar se é um palídromo ou não: '))
palavra2 = palavra1.lower().strip().replace(' ', '')
if palavra2 == palavra2[::-1]:
    print('{} é um palíndromo.'.format(palavra1))
else:
   print('{} não é um palíndromo.'.format(palavra1))