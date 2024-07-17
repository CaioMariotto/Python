#Pedir para o usuário informar o ãngulo a ser calculado e realizar os calculos de sen, coss e tang.
#Imprimir na tela os respectivos resultados.

from math import sin, cos, tan, radians

an=float(input('Digite o ângulo a ser calculado '))
sen     =sin(radians(an))
coss    =cos(radians(an))
tang    =tan(radians(an))

print('O angulo {}\nTem o SENO de {:.2f}\nO COSSENO de {:.2f}\nA TANGENTE de {:.2f}'.format(an,sen,coss,tang))