potencia = int(input('Digite a potência das lâmpadas que serão utilizadas no cômodo: '))

#Dimensões do cômodo
largura = float(input('Digite a largura do cômodo: '))
comprimento = float(input('Digite o comprimento do cômodo: '))

# Cálculo da área do cômodo
area = largura * comprimento

# Número de lâmpadas
n_lampadas = area / potencia

print('A quantidade de lâmpadas necessárias para iluninar o cômodo é de {:.0f}'.format(n_lampadas))