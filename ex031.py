'''Pedir para o usuario informar a distancia em km.
Calcule o preço da passagem cobrando R$0.50 por KM para viagens de ate 200KM e R$0.45 para viagens acima de 200KM. '''

km=int(input('Digite a quilometragem rodada: '))


if km <= 200:
    preço=km*0+50
else:
    preço=km*0.45
print('O preço será R${:.2f}.'.format(preço))
