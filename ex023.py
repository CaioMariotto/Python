import random

num=int(input('Digite um número de 0 à 9999: '))
u=num//1%10
d=num//10%10
c=num//100%10
m=num//1000%10
print('A unidade do número digitado é: {}'.format(u))
print('A dezena do número digitado é: {}'.format(c))
print('A centena do número digitado é: {}'.format(d))
print('A milhar do núemro digtado é: {}'.format(m))