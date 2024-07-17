#Pedir para o usuario informar um numero 
#imprimir na tela se esse numero é par ou impar.

num=int(input('Digite um numero: '))
num1=num%2
if num1==0:
    print('Seu número é par.')
else:
    print('Seu número é ímpar.')
