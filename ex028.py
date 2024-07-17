#Fazer o computador escolher aleatoriamente um numero de 0-5
#Pedir para o usuário informar um numero de 0-5
#Printar na tela se o numero digitado for igual ou nao ao esoclhido pelo computador.

import random

n0=0
n1=1
n2=2
n3=3
n4=4
n5=5

lista=[n0,n1,n2,n3,n4,n5]
num=random.choice(lista)
dig=int(input('Digite um número de 0 a 5: '))
print('O número que o computador escolheu foi: {}.'.format(num))
print('O número que voce escolheu foi {}.'.format(dig))

if num==dig:
    print('Voce acertou o número!')
else:
    print('Voce errou o número!')