'''escreva um programa que leia 2 numeros inteiros e compare-os
mostrando:
- o primeiro valor é maior
- o segundo valor é maior
- nao existe diferença, os valores são iguais'''
num1=int(input('Digite um valor:'))
num2=int(input('Digita um segundo valor: '))

if num1 > num2:
    print('O primeiro valor é maior que o segundo.')
elif num1 < num2:
    print('O segundo valor é maior que o primeiro.')
else:
    print('Não existe diferença, os valores são iguais.')