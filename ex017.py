#Pedir para o usuário informar o cateto oposto e o cateto adjacente e imprimir na tela o calculo da hipotenusa.

from math import hypot

'''co=float(input('Digite comprimento do cateto oposto: '))
ca=float(input('Digite o comprimento do cateto adjacente: '))
hipo= (co**2+ca**2)**(1/2)
print('O valor da hipotenusa é {:.2f}.'.format(hipo))'''

co=float(input('Digite o cateto oposto: '))
ca=float(input('Digite o cateto adjacente '))
hi=hypot(co,ca)
print('A hipotenusa é: {:.2f}'.format(hi))