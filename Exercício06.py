def n_maior(a, b, c):
    maior = a
    if (b > maior):
        maior = b
    elif (c > maior):
        maior = c 
    else:
        pass
    
    return maior

def n_menor(a, b, c):
    menor = a
    if (b < menor):
        menor = b
    elif(c < menor):
        menor = c
    else:
        pass

    return menor

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o último valor: '))

print()
print('O maior dos valores digitados é: ',n_maior(a,b,c))
print('O menor dos valores digitados é: ',n_menor(a,b,c))



# DETERMINAÇÃO DO VALOR INTERMEDIÁRIO
mx = n_maior(a,b,c)
mn = n_menor(a,b,c)

if ((mx != a) and (mn != b)) or ((mx != b) and (mn != a)):
    interm = c
    print('Valor intermediário: {}'. format(interm))
elif ((mx != a) and (mn != c)) or ((mx != c) and (mn != a)):
    interm = b
    print('Valor intermediário: {}'. format(interm))
else:
    intern = a
    print('Valor intermediário: {}'. format(interm))

print()