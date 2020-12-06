'''
Faça um programa para o jogo da velha. Considere dois jogadores que se alternam nas jogadas. 
O primeiro é o “x” e o segundo o “o”. A cada jogada você deve atualizar a visualização do jogo 
da velha e verificar se o jogo chegou ao fim. As opções de finalização são: empate ou vencedor. 
No caso de ter um vencedor, indique qual jogador venceu. A cada jogada permita que o jogador indique 
em qual linha x coluna deseja jogar. Não permita que o jogador insira uma jogada em um local que 
já recebeu uma marcação. Não permita que um jogador jogue duas vezes seguidas tomando a vez do adversário.
Qualquer jogador pode desistir do jogo inserindo algum valor específico para isso. Ele também pode 
encerrar o programa com uma entrada específica. No caso em que ele desiste do jogo, o adversário 
deve ser considerado vencedor e o jogo deve poder ser reiniciado. No caso de saída do programa, 
ele deve parar a execução com uma mensagem de “tchau, até logo!”.
Para ganhar a pontuação, o aluno deve passar pela arguição do professor. De forma que a pontuação 
máxima é 3, mas seu cálculo é o resultado da multiplicação da nota no programa de jogo da velha 
multiplicado pela nota obtida na apresentação. A nota da apresentação varia de 0 até 1.
'''

import sys

print('Bem-vindo(a) ao jogo da velha!\n\n')

def printa_jogo(mat):
    i = 0
    j = 0
    while i < len(mat):
        while j < len(mat[i]):
            if mat[i][j] == -1:
                sys.stdout.write('  | ')
            elif mat[i][j] == 0:
                sys.stdout.write('o' + ' | ')
            elif mat[i][j] == 1:
                sys.stdout.write('x' + ' | ')
            j = j + 1
        print('\n------------')
        j = 0
        i = i + 1

#Verifica linhas, colunas, e diagonais

def jogo_finalizado(mat):
    i = 0
    j = 0

    while i < len(mat):
        if (len(set(mat[i])) == 1):
            if (mat[i][0] != -1):
                return True
        i = i + 1

    #rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))] 
    i = 0
    j = 0

    transposta = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

    print(transposta)

    i = 0
    j = 0
    while j < len(transposta):
        if (len(set(transposta[j])) == 1):
            if (transposta[j][0] != -1):
                return True
        j = j + 1

    # Falta verificar diagonais
    diagonal_principal = [mat[0][0], mat[1][1], mat[2][2]]
    diagonal_secundaria = [mat[0][2], mat[1][1], mat[2][0]]

    if (len(set(diagonal_principal)) == 1):
        if (diagonal_principal[0] != -1):
            return True
    elif (len(set(diagonal_secundaria)) == 1):
        if (diagonal_secundaria[0] != -1):
            return True
    
    return False


jogo = [[-1 for x in range(3)] for y in range(3)] # matriz 3x3

jogo_acabou = False
jogador = 0

print('INSTRUÇÕES: Digite AxB para preencher a linha A na coluna B (exemplo: 0x1, 1x2, 3x4)')

while (jogo_acabou == False):
    printa_jogo(jogo)

    movimentos = 0

    jogada = ''
    jogada_valida = False


    while (jogada_valida == False):
        if (jogador == 0):
            sys.stdout.write('o > ')
        elif (jogador == 1):
            sys.stdout.write('x > ')

        sys.stdout.write('Qual é o seu movimento? ')
        jogada = input()

        jogada = jogada.split('x')
        i = 0

        if (len(jogada) != 2):
            sys.stdout.write('Movimento inválido!\n')
            continue


        jogada[0] = int(jogada[0])
        jogada[1] = int(jogada[1])

        if (jogo[jogada[0]][jogada[1]] != -1):
            sys.stdout.write('Faça um NOVO movimento!\n')
            continue

        jogo[jogada[0]][jogada[1]] = jogador
        jogada_valida = True

    if (jogo_finalizado(jogo)):
        sys.stdout.write('Jogo acabou!\n')
        jogo_acabou = True
        if jogador == 0:
            sys.stdout.write('o venceu!\n')
        elif jogador == 1:
            sys.stdout.write('x venceu! \n')

    if (movimentos >= 10):
            jogo_acabou = True
            sys.stdout.write('Jogo acabou!\n')
            sys.stdout.write('Deu velha!\n')

    movimentos = movimentos + 1
    jogador = ~jogador + 2

    if (jogo_acabou == False):
        print(chr(27)+'[2j')
        #print('\033c')
        #print('\x1bc')

printa_jogo(jogo)