'''
Crie um programa que verifica todos os números perfeitos em um intervalo fornecido pelo usuário. 
Ou seja, o usuário fornece dois valores (inicial e final) e o programa verifica se existe e 
quais são os números perfeitos nesse intervalo. Para saber o que são números perfeitos, busque na wikipedia.
'''

def perfect():

    ni = int(input('Digite o valor inicial do intervalo: '))
    nf = int(input('Digite o valor final do intervalo: '))
    
    print('Determinar quantos números são perfeitos dentro do intervalo {} e {}'.format(ni, nf))

    n = ni
    contador = 0

    while n <= nf:

        n += 1      # n = n + 1
        soma = 0
  
        for divisor in range(1,n):
            if n % divisor == 0:
                soma += divisor     # soma = soma + divisor

        if n == soma:
            print('O número {} é um número perfeito.'.format(n))
            contador += 1
        else: 
            pass
        
    print('No intervalo entre {} e {} existem {} números perfeitos.'.format(ni, nf, contador))
perfect()