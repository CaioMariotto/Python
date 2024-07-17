#Pedir para o usuário informar a temperatura e imprimir na tela em Celcius e fahrenheit.

c=float(input('Informe a temperatura '))
f=((c*9)/5)+32

print('A temperatura de {}°C corresponde a {}°F'.format(c,f))
