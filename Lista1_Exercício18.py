nota1 = float(input('Digite a nota da primeira prova realizada pelo estudante: '))
nota2 = float(input('Digite a nota da segunda prova realizada pelo estudante: '))
nota3 = float(input('Digite a nota da prova optativa ou -1 caso o estudante não a tenha feito: '))

if nota3 == -1:
    media = (nota1 + nota2) / 2
else:
    if nota1 > nota2:
        media = (nota1 + nota3) / 2
    else: 
        media = (nota2 + nota3) / 2

print(nota1, nota2, nota3, media)

if media >= 6.0:
    print('Aprovado')
elif media < 3.0:
    print('Reprovado')
else:
    print('Em Exame')