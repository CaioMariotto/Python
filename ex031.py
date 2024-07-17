#Pedir para o usuario informar a distancia em km.
#Calcule o preço da passagem cobrando R$0.50 por KM para viagens de ate 200KM e R$0.45 para viagens acima de 200KM.

km=int(input('Digite a quilometragem rodada: '))
lim=200

if km <= lim:
    print('Voce rodou {}km, seu pagamento será de {} reais.'.format(km,km*0.50))
else:
    print('Voce rodou {}km e seu pagamento será de {} reais.'.format(km,((km-lim)*0.45)+100))

