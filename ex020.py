#escolher aleatoriamente 1 dentre as 4 opçoes de nome.
#Depois disso, imprimir na tela o resultado.

from random import shuffle

nome1='laura'
nome2='jose'
nome3='maria'
nome4='bia'

lista=[nome1, nome2, nome3, nome4]
shuffle(lista)

print('A ordem será: ')
print(lista)