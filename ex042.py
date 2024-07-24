'''refaça o exercicio 35
acrescentando o recurso de mostrar o tipo de triangulo que sera formado'''

r1=int(input('digite o valor da primeira reta: '))
r2=int(input('digite o valor da segunda reta: '))
r3=int(input('digite o valor de uma ultima reta: '))

r1, r2, r3

if (r1 == r2 == r3):
    print(f'O triangulo é EQUILATERO')
elif (r1 == r2 or r2 == r3 or r1 == r3):
    print(f'O triangulo é ISÓSCELES')
else:
    print(f'O triangulo é ESCALENO')
