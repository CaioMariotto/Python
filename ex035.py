#leia o comprimento de tres retas 
#e diga ao usuario se elas podem ou nao formar um triangulo

r1=int(input('digite o valor de uma reta: '))
r2=int(input('digite o valor de outra reta: '))
r3=int(input('digite o valor de uma ultima reta: '))

r1, r2, r3

if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
        print('Da pra montar um triangulo.')
else:
        print('Não da pra montar um triangulo.')