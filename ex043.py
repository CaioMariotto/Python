'''Desenvolva um programa que leia o peso e altura da pessoa
calcule e mostre o seu IMC e mostre seu status de acordo com a tabela abaixo
- abaixo de 18.4: baixo do peso
- de 18.5 e 24.9: peso ideal
- de 25 ate 29.9: sobrepeso
- de 30 ate 39.9: obesidade
- acima de 40: obesidade morbida'''


altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))
imc = (peso // (altura**2))

if imc <= 18.4:
    print(f'Voce está abaixo do peso.')
elif imc >= 18.5 and imc <= 24.9:
    print('Seu IMC é {} e voce está no peso ideal.'.format(imc))
elif imc >= 25 and imc <= 29.9:
    print('Seu IMC é {} e voce esta com sobrepeso.'.format(imc))
elif imc >= 30 and imc <= 39.9:
    print('Seu IMC é {} e voce esta com obesidade.'.format(imc))
else:
    print('Seu IMC é {} e voce está com obesidade morbida.'.format(imc))