vel=int(input('Qual a velocidade do veículo: '))
limite=80

if vel > limite:
    print('Você foi multado por andar acima da velocidade permitida de 80 KM/h.')

if vel>limite:
    print('A velocidade passou em {} KM/h a velocidade limite.'.format(vel-limite))
print('Você foi multado em {} reais.'.format((vel-limite)*7))
