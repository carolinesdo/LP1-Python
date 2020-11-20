c = 1.90
inicial = int(input('Digite o valor inicial do odômetro: '))
final = int(input('Digite o valor final do odômetro: '))
od = final - inicial
combustivel = float(input('Digite a quantidade de combustível gasta durante o dia: '))
lucro = float(input('Digite o valor ganho hoje: '))
media = od / combustivel
lucroliquido = lucro - (c * combustivel)

print('Durante o dia o carro percorreu {} km, teve um consumo médio de  {:.2f} km/l e o lucro líquido do motorista foi de R$ {}'.format(od, media, lucroliquido))
