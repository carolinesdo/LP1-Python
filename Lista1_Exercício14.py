ang1 = int(input('Digite o primeiro valor do ângulo interno do triângulo: '))
ang2 = int(input('Digite o segundo valor do ângulo interno do triângulo: '))
ang3 = int(input('Digite o terceiro valor do ângulo interno do triângulo: '))

# TESTE PARA VERIFICAR SE OS VALORES ANGULARES DIGITADOS FORMAM UM TRIÂNGULO
triangulo = ang1 + ang2 + ang3

if triangulo == 180:
    # CLASSIFICAÇÃO DOS TRIÂNGULOS
    if ang1 < 90 and ang2 < 90 and ang3 < 90:
        print ('Triângulo agudo')
    elif ang1 == 90 or ang2 == 90 or ang3 == 90:
        print('Triângulo reto')
    else:
        print('Triângulo obtuso')
else:
    print('Os valores angulares digitados não formam um triângulo!')
