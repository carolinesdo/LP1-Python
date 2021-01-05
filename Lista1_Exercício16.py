comprimento = float(input('Digite o comprimento da parede do cômodo: '))
largura = float(input('Digite a largura da parede do cômodo: '))
altura = float(input('Digite a altura da parede do cômodo: '))

caixa = 1.5

area_paredes = 2 * (comprimento * altura) + 2 * (largura * altura)

quantidade_caixas = area_paredes / caixa

print('Para este cômodo serão necessárias {:.0f} caixas de azulejo'.format(quantidade_caixas))
