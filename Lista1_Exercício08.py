print('Programa para ler uma temperatura em Celsius e retornar os valores destas temperaturas em Fahrenheit e Kelvin')
celsius = float(input('Digite a temperatura, em Celsius: '))
kelvin = celsius + 273
fahrenheit = ((9/5) * celsius) + 32

print('Temperatura em Celsius: {:.1f}° C; Temperatura em Fahrenheit: {:.1f}° F; Temperatura em Kelvin: {:.1f} K'.format(celsius, fahrenheit, kelvin))