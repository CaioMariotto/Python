from math import sin, cos, tan, radians

an=float(input('Digite o ângulo a ser calculado '))
sen     =sin(radians(an))
coss    =cos(radians(an))
tang    =tan(radians(an))

print('O angulo {}\nTem o SENO de {:.2f}\nO COSSENO de {:.2f}\nA TANGENTE de {:.2f}'.format(an,sen,coss,tang))